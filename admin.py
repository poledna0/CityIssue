import sqlite3

DB_PATH = "cityissue.db"

def listar_usuarios(cursor):
    cursor.execute("""
        SELECT id, nome, email, role
        FROM users
        ORDER BY nome
    """)

    usuarios = cursor.fetchall()

    print("\n=== USUÁRIOS ===")
    for usuario in usuarios:
        print(
            f"ID: {usuario[0]}\n"
            f"Nome: {usuario[1]}\n"
            f"Email: {usuario[2]}\n"
            f"Role: {usuario[3]}\n"
            f"{'-'*50}"
        )

def promover_para_admin(cursor, conn, user_id):
    cursor.execute(
        "UPDATE users SET role = 'admin' WHERE id = ?",
        (user_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("\nUsuário promovido para admin com sucesso!")
    else:
        print("\nNenhum usuário encontrado com esse ID.")

def main():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        listar_usuarios(cursor)

        user_id = input(
            "\nDigite o ID do usuário que deseja transformar em admin: "
        ).strip()

        confirmar = input(
            f"Tem certeza? (s/n): "
        ).lower()

        if confirmar == "s":
            promover_para_admin(cursor, conn, user_id)

            print("\n=== LISTA ATUALIZADA ===")
            listar_usuarios(cursor)
        else:
            print("Operação cancelada.")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    main()