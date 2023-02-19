from collections import Counter

members = []

with open("members.txt", "r") as f:
    for member in f:
        members.append(member.strip())
members_set = set(members)

friends = {m:set([m]) for m in members}

friendships_file = "friends05.txt"
if input("Select longer friendlist (friends10.txt)? (y/yes): ").lower() in ("y", "yes"):
    friendships_file = "friends10.txt"

with open(friendships_file, "r") as f:
    for friendship in f:
        a, b = friendship.strip().split()
        friends[a].add(b)
        friends[b].add(a)


def solve_max_matching(member_set, clique, selected, limit):
    if limit == 0 or len(selected) >= len(clique) or len(member_set) == 0:
        return set.intersection(clique, set(selected))
    selection = member_set.pop()
    # member_set.remove(selection)
    if selection in clique:
        selected.append(selection)
        result1 = solve_max_matching(member_set, set.intersection(clique, friends[selection]), selected, limit-1)
        selected.pop()
    else:
        result1 = set()
    result2 = solve_max_matching(member_set, clique, selected, limit)
    member_set.add(selection)
    if len(result1) > len(result2):
        return result1
    return result2

friend_count = [len(friends[member]) for member in members]
# max_degree = max(len(x) for x in friends.values())
# max_degree = max(friend_count)

degree_counts = Counter(friend_count)
degrees = sorted(degree_counts.keys(), reverse=True)
degree_members = {d: [] for d in degrees}
for i in range(len(members)):
    degree_members[friend_count[i]].append(members[i])

best_result = set()
limit = 1
result = solve_max_matching(set(members), members_set, [] , limit)
while len(result) > len(best_result):
    print("Improving result to ", len(result), "->", result)
    best_result = result

    limit += 1
    result = solve_max_matching(set(members), members_set, [] , limit)
print("Result not improved for bound", limit)

print("Largest clique has size", len(best_result), "e.g. the following members form one such clique:", ", ".join(sorted(best_result)))
