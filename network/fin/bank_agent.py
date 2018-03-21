import random

import structures.bs_constants as bst
from network.core.skeleton import Node
from products.equities import Stock
from structures.bank_structures import BalanceSheet


def upset(ln, num, den):
    ln.value -= ln.value * num / den


class Bank(Node):
    def __init__(self, name, unique_id, model, data, time_series):
        super().__init__(unique_id, model)
        self.name = name
        self.time_series = time_series
        self.balance_sheet = BalanceSheet(data, "BS")
        self.interbankAssets = self.balance_sheet.find_node_series("Assets", "Interbank")
        self.interbank_borrowing = self.balance_sheet.find_node_series("Liabilities", "Interbank")
        self.externalAssets = self.balance_sheet.find_node_series("Assets", "External")
        self.capital = self.balance_sheet.find_node("Equities")
        self.customer_deposits = self.balance_sheet.find_node_series("Liabilities", "Deposits and Others")
        self.shock = 0.0
        self.defaults, self.affected = False, False
        self.counter_parties = []
        self.bad_debt = 0.0
        self.issued_shares = self.capital.value
        self.price_history = [1.0]
        self.stock = Stock(S=1.0, mu=time_series.mu, std=time_series.vol, dt=1.0 / 252.)
        self.unallocated_credit = self.balance_sheet.find_node_series("Liabilities", "Interbank").value
        self.unallocated_debt = self.balance_sheet.find_node_series("Assets", "Interbank").value

    def equity_change(self):
        if self.defaults:
            self.price_history.append(self.stock.S)
            return
        init__s = self.stock.S
        self.stock.evolve()
        common = self.capital.find_node(bst.common_stock)
        other = self.capital.find_node_series(bst.other_equity)
        preferred = self.capital.find_node_series(bst.preferred_stock)
        total = sum([x.value for x in [common, other, preferred]])
        delta = (self.stock.S - init__s) * self.issued_shares
        for x in [common, other, preferred]:
            if x.value != 0.0:
                value_total = delta * x.value / total
                x.value += value_total
        self.balance_sheet.find_node(bst.cash_and_cash_equivalents).value += delta
        self.price_history.append(self.stock.S)
        self.balance_sheet.re_aggregate()

    def apply_shock(self):
        if self.defaults:
            return
        if random.random() > .99:
            self.shock = self.balance_sheet.find_node("Equities").value/4

    def deal_with_shock(self, tremor=True):
        if self.defaults:
            return
        # If no shock felt by bank, return
        equity_impact = 0.0
        recovery = 0.6
        if self.shock == 0.0:
            return
        # if shock is resulting from interbank reverberations ----
        self.affected = True
        if tremor:
            liquid_external_assets = self.balance_sheet.find_node_series("Assets", "External", "Liquid")
            disbursable = max(0.0, min(liquid_external_assets.value, self.shock))
            liquid_nodes = liquid_external_assets.get_all_terminal_nodes()
            for ln in liquid_nodes:
                ln.value -= ln.value * disbursable / liquid_external_assets.value
            equity_impact += disbursable
            self.shock -= disbursable
            # if shock cannot be absorbed by liquid assets
            if self.shock > 0.0:
                illiquid_external_assets = self.balance_sheet.find_node_series("Assets", "External", "Illiquid")
                disbursable = min(self.shock, illiquid_external_assets.value * recovery)
                for iln in illiquid_external_assets.get_all_terminal_nodes():
                    iln.value -= iln.value * (disbursable / recovery) / illiquid_external_assets.value

                equity_impact += disbursable / recovery
                self.shock -= disbursable
                if self.shock > 0.0:
                    self.deal_with_bankruptcy(self.shock)

            equity = self.balance_sheet.find_node_series("Equities")
            if equity.value < equity_impact:
                self.defaults = True
                # equity_impact = equity.value
            for eqty in equity.children:
                eqty.value -= equity_impact * eqty.value / equity.value
            self.balance_sheet.re_aggregate()
            self.stock.S = equity.value / self.issued_shares

    def deal_with_bankruptcy(self, residual):
        self.process_bankruptcy(residual)
        # self.borrow_to_offset(residual)

    def process_bankruptcy(self, residual):
        self.defaults = True
        self.shock = 0.0
        edge_vals = sum([y.value for y in self.edges if  not y.node_to.defaults])
        for x in self.edges:
            if x.node_to.defaults:
                continue
            else:
                shock_val = residual * x.value / edge_vals
                x.node_to.shock += shock_val
                x.value -= shock_val

    def borrow_to_offset(self, residual):
        all_agents = self.model.schedule.agents
        viable_lenders = [agt for agt in all_agents if agt.externalAssets.value > 2 * residual]
        if viable_lenders:
            lender = random.choice(viable_lenders)
            edge = self.edge_exists(lender)
            edge.value += residual
            self.interbank_borrowing.value += residual
            self.externalAssets.value += residual
            lender.interbankAssets.value += residual
            lender.externalAssets.value += residual
        else:
            self.process_bankruptcy(residual)

    def collect_debts(self, residual):
        total_loans = sum(x.value for x in self.in_degree)
        fract = residual / total_loans
        if fract < 1:
            for x in self.in_degree:
                temp = x.value
                x.value -= fract * x.value
                x.node_from.interbank_borrowing.value -= temp * fract
            self.interbankAssets.value -= total_loans * fract
            return residual
        else:
            for x in self.in_degree:
                self.remove_edge(x)
                x.node_from.interbank_borrowing.value -= x.value
            return total_loans
