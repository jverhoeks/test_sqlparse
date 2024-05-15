import sqlglot.expressions as exp
import sqlglot

from sqlglot.optimizer import optimize


# def qualify_columns(expression, schema):
#     try:
#         expression = sqlglot.optimizer.qualify_tables.qualify_tables(expression)
#         expression = sqlglot.optimizer.isolate_table_selects.isolate_table_selects(expression)
#         expression = sqlglot.optimizer.qualify_columns.qualify_columns(expression, schema)

#     except (OptimizeError) as e:
#         pass

#     return expression

def _is_create_table_ddl(statement: sqlglot.exp.Expression) -> bool:
    return isinstance(statement, sqlglot.exp.Create) and isinstance(
        statement.this, sqlglot.exp.Schema
    )

def parse_sql(file_name,dialect):


    with open(file_name, "r") as file:
        query = file.read()


    for expression in sqlglot.parse(query):
        parse_ddl(expression)


def parse_ddl(expression):

    if isinstance(expression, sqlglot.exp.Create):
        if _is_create_table_ddl(expression):
            print("DDL")

            #ast = qualify_columns(node, schema = None)
            ast = optimize(expression,None)
            #print(repr(ast))
            print(ast.sql())

            create_schema: exp.Schema = expression.this
            sqlglot_columns = create_schema.expressions

            for column_def in sqlglot_columns:
                col = {}

                if not isinstance(column_def, sqlglot.exp.ColumnDef):
                    # Ignore things like constraints.
                    print(column_def)
                    continue

                col['name'] = column_def.name
                col['type'] = column_def.kind.this.name

                col['quoted'] = column_def.this.is_string

                for dt in column_def.find_all(exp.DataTypeParam):
                    col['length'] = int(dt.this.name)

                for contraint in column_def.constraints:
                    #print(repr(contraint.kind))
                    col['primary_key'] = isinstance(contraint.kind,exp.PrimaryKeyColumnConstraint)
                    col['nullable'] = not isinstance(contraint.kind,exp.NotNullColumnConstraint)
                    col['default'] = isinstance(contraint.kind,exp.DefaultColumnConstraint)


                print(col)



def main():
    parse_sql("data.sql","postgresql")
    parse_sql("snowflake.sql","snowflake")
    parse_sql("athena.sql","athena")

if __name__ == "__main__":
    main()