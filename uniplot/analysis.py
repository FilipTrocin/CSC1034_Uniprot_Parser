def average_len(records):
     """Returns the average length of the proteins"""
     average = sum(len(record) for record in records) / len(records)
     return average


def average_len_taxa(records):
    """Returns the average length of top-level taxas"""
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][0]
        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
