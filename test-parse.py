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
            print(repr(ast))
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
                # get the type of the column
                col['type'] = column_def.kind.this.name

                # if string that means spaces or other chars in the fieldname
                #col['quoted'] = column_def.this.is_string

                for dt in column_def.find_all(exp.DataTypeParam):
                    col['maxLength'] = int(dt.this.name)

                if column_def.kind.this.name == "ENUM":
                    col['enum'] = [x.name for x in column_def.kind.expressions]

                # get the constraints
                for contraint in column_def.constraints:
                    #print(repr(contraint.kind))
                    col['primary'] = isinstance(contraint.kind,exp.PrimaryKeyColumnConstraint)
                    col['required'] = isinstance(contraint.kind,exp.NotNullColumnConstraint)
                    col['unique'] = isinstance(contraint.kind,exp.UniqueColumnConstraint)

                    if isinstance(contraint.kind,exp.CommentColumnConstraint):
                        col['description'] = contraint.kind.name

                    if isinstance(contraint.kind,exp.DefaultColumnConstraint):
                        col['default'] = contraint.kind.name


                # fields/items)
                print(col)


# Unicode character sequence: string, text, varchar
# Any numeric type, either integers or floating point numbers: number, decimal, numeric
# 32-bit signed integer: int, integer
# 64-bit signed integer: long, bigint
# Single precision (32-bit) IEEE 754 floating-point number: float
# Double precision (64-bit) IEEE 754 floating-point number: double
# Binary value: boolean
# Timestamp with timezone: timestamp, timestamp_tz
# Timestamp with no timezone: timestamp_ntz
# Date with no time information: date
# Array: array
# Sequence of 8-bit unsigned bytes: bytes
# Complex type: object, record, struct
# No value: null


def main():
    parse_sql("data.sql","postgresql")
    parse_sql("snowflake.sql","snowflake")
    parse_sql("athena.sql","athena")
    parse_sql("mysql.sql","mysql")

if __name__ == "__main__":
    main()