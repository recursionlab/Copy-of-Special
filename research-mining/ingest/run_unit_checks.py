from dedupe_cluster import text_signature, tokenize, jaccard, dedupe_units, cluster_jaccard, aggregate_cluster


def run_checks():
    # tokenize/jaccard
    a = tokenize("Recursive loops and feedback")
    b = tokenize("feedback loops in recursion")
    assert "recursive" in a
    assert jaccard(a, b) > 0

    # dedupe
    u1 = {"id":"a","definition":"Same def"}
    u2 = {"id":"b","definition":"Same def"}
    deduped, hmap = dedupe_units([u1, u2])
    assert len(deduped) == 1 and len(hmap) == 1

    # cluster + aggregate
    u1 = {"id":"a","definition":"apple banana cherry","tags":["fruit"],"references":[{"r":1}],"notes":"n1","confidence_score":0.9}
    u2 = {"id":"b","definition":"apple banana","tags":["fruit","food"],"references":[{"r":1}],"notes":"n2","confidence_score":0.7}
    u3 = {"id":"c","definition":"quantum field theory","tags":["physics"],"references":[],"notes":None,"confidence_score":0.8}
    units = [u1,u2,u3]
    deduped, hmap = dedupe_units(units)
    clusters = cluster_jaccard(deduped, threshold=0.3)
    assert any(len(c) >= 2 for c in clusters)
    agg = aggregate_cluster(deduped, clusters[0])
    assert "members" in agg and "tags" in agg

    print("ALL CHECKS PASSED")

if __name__ == '__main__':
    run_checks()
