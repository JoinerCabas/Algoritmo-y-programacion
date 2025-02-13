Algoritmo Ejercicio_11_Sueldo_Trabajador
	//Entradas
	Escribir "Nombre del trabajador: "
    Leer NombreTrabajador
    Escribir "Numero de horas normales trabajadas: "
    Leer HorasNormales
    Escribir "Pago por hora normal:  "
    Leer PagoHoraNormal
    Escribir "Numero de horas extras trabajadas:"
    Leer HorasExtras
	Escribir "Numero de hijos del trabajador:"
    Leer NumeroDeHijos
   //Caja Negra
    PagoHoraExtra <- PagoHoraNormal * 1.25
    SueldoBase <- (HorasNormales * PagoHoraNormal) + (HorasExtras * PagoHoraExtra)
    Asignaciones <- 250000 + (173000 * NumeroDeHijos) + 180000
    DeductionPagForzoso <- SueldoBase * 0.05
    DeductionPolHabitacional <- SueldoBase * 0.02
    DeductionCajaAhorro <- SueldoBase * 0.07
    TotalDeducciones <- DeductionPagForzoso + DeductionPolHabitacional + DeductionCajaAhorro
    SueldoNeto <- SueldoBase + Asignaciones - TotalDeducciones
   //Salidas
    Escribir "Nombre del trabajador: ", NombreTrabajador
    Escribir "Sueldo Base: ", SueldoBase
    Escribir "Asignaciones: ", Asignaciones
    Escribir "Deducciones: ", TotalDeducciones
    Escribir "Sueldo Neto: ", SueldoNeto
FinAlgoritmo
