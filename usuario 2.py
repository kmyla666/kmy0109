usuarios_permitidos = {
    'pedro': '1234',
    'angel': 'a4s1'
}

nombre_usuario = input('Ingrese su nombre de usuario: ')
contraseña = input('Ingrese su contraseña: ')
if nombre_usuario in usuarios_permitidos and usuarios_permitidos[nombre_usuario] == contraseña:
    print('Acceso permitido , bienvenido')
else:
    print("Acceso denegado, intentelo nuevamente")
