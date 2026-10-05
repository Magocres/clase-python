# Esto muestra por consola este mensaje
#print("Hola mundo !")

nombre : str = "Mario";
apellido : str = "González";
edad : int = 22;
ciudad : str = "Valencia";
tengo_carnet : bool = True;

#print(f"Hola, me llamo {nombre} {apellido} y tengo {edad} años");
#print(type(nombre));

#print(nombre.upper());
#print(len(nombre));
#print(nombre[0]);
#print(apellido[-1]);

persona : dict[str, str | int | bool] = {
    "nombre": "Mario",
    "edad": 22,
    "ciudad": "Valencia",
    "solterx": True
}

#print(persona["nombre"]);

compra = ["pan", "leche", "huevos"];
compra.append("frutas");
compra.insert(1, "verduras");
compra.pop(-1);
#print(compra);

culpable : bool = True;

#if culpable:
#    print("Es culpable");
#else:
#    print("No es culpable");