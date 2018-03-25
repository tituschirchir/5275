# Allocate debt and credit in batches to avoid overallocation to one entity
def allocate(banks):
    batches = 100
    [allocate_debt_for_bank(bank, batches) for i in range(batches) for bank in banks]
    [allocate_debt_for_bank(bank, 1) for bank in banks]


def allocate_debt_for_bank(bank, batches):
    debt_for_session = bank.balance_sheet.find_node_series("Assets", "Interbank").value / batches
    nearby_credit = sum([x.node_to.unallocated_credit for x in bank.edges])
    to_operate = min(bank.unallocated_debt, debt_for_session)
    allocatable = min(to_operate, nearby_credit)
    if nearby_credit > 0.0:
        for edge in bank.edges:
            d2 = round(allocatable * edge.node_to.unallocated_credit / nearby_credit, 4)
            edge.value += d2
            edge.node_to.unallocated_credit -= d2
            bank.unallocated_debt -= d2
