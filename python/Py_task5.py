from multiprocessing import Pool
def transform(record):
    return record*record
records=list(range(10_000_000))
with Pool(6) as pool:
    results=pool.map(transform,records)
print(results[:10])
