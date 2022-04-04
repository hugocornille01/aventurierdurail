from aventurierdurail import AventurierDuRail
from graph import Graph

aventurierDuRail = AventurierDuRail("aventurierdurail.json")
total = Graph()
for path in aventurierDuRail.Paths:
    total.Paths.append(path)

print(total.Paths)
print(total.Towns)
print(total.getTotalWeight())