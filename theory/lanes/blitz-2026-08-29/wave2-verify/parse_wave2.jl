files = [
    "numerics/src/lambdaD_edge.jl",
    "numerics/src/lambdaD_memory.jl",
    "numerics/src/lambdaD_memory_run.jl",
    "numerics/scripts/run_lambdaD_memory.jl",
    "numerics/test/test_lambdaD_memory.jl",
]

for file in files
    source = read(file, String)
    tree = Meta.parseall(source; filename = file)
    @assert tree isa Expr
    println("PARSE PASS: ", file)
end
