using Test

# Auto-discover shard test files so that concurrently-landing shards are picked
# up without editing this file.
@testset "TriangleMPS" begin
    for f in sort(filter(f -> startswith(f, "test_") && endswith(f, ".jl"),
                         readdir(@__DIR__)))
        include(joinpath(@__DIR__, f))
    end
end
