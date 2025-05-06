Usuarios = {
    "iperurena": {"nombre": "Iñaki", "apellido": "Perurena", "password": "123123"},
    "fmuguruza": {"nombre": "Fermín", "apellido": "Muguruza", "password": "654321"},
    "aolaizola": {"nombre": "Aimar", "apellido": "Olaizola", "password": "123456"},
}
def comprobar_informacion(nombre_usuario: str, password: str) -> bool:
    nombre_usuario = nombre_usuario.strip().lower() 
    datos_usuario = Usuarios.get(nombre_usuario)
    if datos_usuario and datos_usuario["password"] == password:
        return True
    return False
intentos = 1
while intentos <= 3:
    nom_usuario = input("Ingrese nombre de usuario: ").strip().lower()
    contraseña = input("Ingrese contraseña: ").strip()
    if comprobar_informacion(nom_usuario, contraseña):
        nombre = Usuarios[nom_usuario]["nombre"]
        apellido = Usuarios[nom_usuario]["apellido"]
        print(f"Bienvenido {nombre} {apellido}")
        break
    else:
        print(f"Usuario o contraseña incorrecta. Intentos restantes: {3 - intentos}")
        intentos += 1
else:
    print("Acceso Denegado")