
from sqlglot.expressions import Create,Schema,Table,Identifier,DataType,ColumnDef
from sqlglot import parse_one

sql = "create table ucx_cbhpy.ucx_swwdo.ucx_tzbiz (value2 varchar(255))"
print(parse_one(sql))


print(repr(parse_one(sql)))

out = Create(
  this=Schema(
    this=Table(catalog="ucx_cbhpy", db="ucx_swwdo", name="ucx_tzbiz"),
    expressions=[
      ColumnDef(
        this=Identifier(this="value2", quoted=False),
        kind=DataType(
          this=DataType.Type.VARCHAR,
          nested=False))]),
  kind="TABLE")

print(out.sql())


# node.select("c", copy=False)
# # low-level
# node.set("expressions", node.expressions + [exp.column("c")])
# node.append("expressions", exp.column("c"))
# node.replace(node.copy().select("c"))

col = ColumnDef(
        this=Identifier(this="value3", quoted=False),
        kind=DataType(
          this=DataType.Type.VARCHAR,
          nested=False))
out.append("expressions", col)
print(out.sql())