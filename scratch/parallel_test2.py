import multiprocessing as mp

DLL_PATH = r"C:\Users\glddm\source\repos\OptimalDecompression\TrinomialModel\bin\Debug\net462\TrinomialModel.dll"

def init_worker():
    import clr
    clr.AddReference(DLL_PATH)
    print(f"Worker {mp.current_process().name}: DLL loaded", flush=True)

def test_call(x):
    # just test the DLL is accessible
    # replace with your actual F# call
    return float(x * 2)

if __name__ == "__main__":
    print("Starting pool", flush=True)
    ctx = mp.get_context("spawn")
    with ctx.Pool(2, initializer=init_worker) as pool:
        results = pool.map(test_call, [1.0, 2.0, 3.0])
    print(f"Results: {results}", flush=True)