<h1 align="center"> 💰 ArgBroker Demo</h1>

Debido a la necesidad de ISPC Cba de la creación de una aplicación que realice transacciones entre inversores, al inscribirse como broker ante la Bolsa de Valores de Buenos Aires MERVAL. Hemos desarrollado ARgBroker Demo, una plataforma demostrativa del proceso de inversión y compra de acciones, permitiendo al usuario comprender el mercado y sus transacciónes sin enfrentarse al riesgo financiero que suponen estas acciones económicas.


<h2>Propuesta formal para el desarrollo de un broker demo</h2>
<h3>🚧 Objetivo: </h3>

El objetivo principal de este proyecto es desarrollar una aplicación que simule la experiencia de operar en la bolsa de valores argentina. La aplicación permitirá a los usuarios:

1. Crear una cuenta: Los usuarios podrán crear una cuenta con un saldo inicial simulado de $1.000.000 para comenzar a invertir.
2. Consultar cotizaciones: Accederán a cotizaciones de acciones de empresas argentinas en tiempo real, lo que les permitirá tomar decisiones informadas de inversión.
3. Realizar transacciones: Podrán realizar operaciones de compra y venta de acciones a precios de mercado, simulando la experiencia real del trading.
4. Gestionar su portafolio: Visualizarán su portafolio de inversiones, incluyendo el total invertido, el saldo de la cuenta y las ganancias o pérdidas obtenidas.
5. Calcular comisiones: La aplicación calculará automáticamente la comisión del broker del 1.5% por cada operación realizada.

<h3>🚧 Beneficios:</h3>

Esta aplicación ofrecerá diversos beneficios a sus usuarios, entre ellos:

1. Aprendizaje sin riesgos: Permite a los usuarios aprender sobre el mercado de valores y practicar estrategias de inversión sin arriesgar dinero real.
2. Desarrollo de habilidades: Brinda la oportunidad de desarrollar habilidades de análisis financiero y toma de decisiones en un entorno simulado.
3. Prueba de estrategias: Facilita la prueba de diferentes estrategias de inversión antes de aplicarlas en el mercado real.
4. Experiencia realista: Simula la experiencia real del trading, permitiendo a los usuarios familiarizarse con las plataformas y herramientas utilizadas en el mercado bursátil.

<h3>🚧 Público objetivo:</h3>

La aplicación está dirigida a un público amplio que incluye:

1. Inversores principiantes: Aquellos que desean aprender sobre el mercado de valores y practicar inversiones sin riesgos.
2. Estudiantes de finanzas: Que buscan una herramienta para complementar sus estudios y desarrollar habilidades prácticas.
3. Inversores experimentados: Que quieren probar nuevas estrategias o familiarizarse con plataformas de trading específicas.

<h3>🚧 Funcionalidades:</h3>
<h3>❗ Funcionalidades:</h3>

1. Registro de usuarios: Permite a los usuarios crear una cuenta con un saldo inicial simulado.
2. Consulta de cotizaciones: Facilita la consulta de cotizaciones de acciones de empresas argentinas en tiempo real.
3. Ejecución de transacciones: Permite realizar operaciones de compra y venta de acciones a precios de mercado.
4. Gestión de portafolio: Brinda la posibilidad de visualizar el portafolio de inversiones, incluyendo el total invertido, el saldo de la cuenta y las ganancias o pérdidas obtenidas.
5. Cálculo de comisiones: Calcula automáticamente la comisión del broker del 1.5% por cada operación realizada.

<h3>❗ Datos:</h3>

 1. Información de usuarios: Almacena datos como nombre, apellido, correo electrónico, contraseña y saldo de cuenta.

 2. Datos de acciones: Guarda información como símbolo, nombre de la empresa, precio de mercado y volumen de negociación.
   
 3. Historial de transacciones: Registra las operaciones de compra y venta de acciones realizadas por los usuarios.
   
 4. Información de portafolio: Mantiene información del portafolio de inversiones de cada usuario, incluyendo el total invertido, el saldo de la cuenta, las ganancias o pérdidas obtenidas y las acciones que posee.

<h3>🚧 Nomeclatura:</h3>
Para el desarrollo del proyecto, se ha acordado la siguiente nomenclatura:

- Clases: Nombres en <b>CamelCase.</b>
- Atributos y Métodos en <b>snake_case.</b>

<h3>🚧 Diseño del Sistema:</h3>
<h3>❗ Diagramas de clases:</h3>


Los diagramas de clases representan las entidades del sistema, sus atributos, métodos y relaciones. Se han utilizado para definir las clases principales del sistema, incluyendo:

- Usuario: Representa a los usuarios del sistema, con atributos como nombre, apellido, correo electrónico, contraseña y saldo de cuenta.
- Acción: Representa las acciones de las empresas argentinas que cotizan en bolsa, con atributos como símbolo, nombre de la empresa, precio de mercado y volumen de negociación.
- Transacción: Representa las operaciones de compra y venta de acciones realizadas por los usuarios, con atributos como fecha, hora, tipo de operación, símbolo de la acción, cantidad de acciones y precio de mercado.
- Portafolio: Representa el portafolio de inversiones de cada usuario, con atributos como el total invertido, el saldo de la cuenta, las ganancias o pérdidas obtenidas y las acciones que posee.

<h3>❗ Modelo relacional:</h3>

El modelo relacional define la estructura de la base de datos, utilizando tablas para almacenar los datos de las entidades del sistema. Las principales tablas incluyen:

- Usuarios: Almacena información de los usuarios, como nombre, apellido, correo electrónico, contraseña y saldo de cuenta.
- Acciones: Almacena información de las acciones de las empresas argentinas, como símbolo, nombre de la empresa, precio de mercado y volumen de negociación.
- Transacciones: Almacena información de las operaciones de compra y venta de acciones realizadas por los usuarios, incluyendo fecha, hora, tipo de operación, símbolo de la acción, cantidad de acciones y precio de mercado.
- Portafolios: Almacena información del portafolio de inversiones de cada usuario, incluyendo el total invertido, el saldo de la cuenta, las ganancias o pérdidas obtenidas y las acciones que posee.

<h3>❗ Suposiciones y decisiones de diseño:</h3>

- Se ha supuesto que los datos de los usuarios y las acciones se actualizarán en tiempo real.
- Se ha decidido utilizar un modelo relacional para la base de datos debido a su simplicidad y flexibilidad.
- Se ha optado por utilizar diagramas de clases para representar el diseño del sistema, ya que son una herramienta visual que facilita la comprensión.

<h2>Autores:</h2>

Este proyecto ha sido desarrollado por los estudiantes del módulo de Programador en ISPC Cba, trabajando de manera colaborativa y asignando tareas específicas a cada miembro del equipo:

<div align="center"> 
 
|Nombre y Apellido|Rol|Correo|Perfil Personal|
|:---:|:---:|:---:|:---:|
|Franco Arce|![](https://img.shields.io/badge/Coordinador-black?style=for-the-badge) <br> ![](https://img.shields.io/badge/Base%20de%20datos-yellow?style=for-the-badge)|[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:francogonzaloarce@gmail.com) | [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Franco-Arce)|
|Eliana Di Lorenzo|![](https://img.shields.io/badge/Coordinador-black?style=for-the-badge) <br> ![](https://img.shields.io/badge/Programación-blue?style=for-the-badge) |[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dilorenzoeliana@gmail.com) | [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ElianaDLV)|
|Gabriel Burgos|![](https://img.shields.io/badge/Ética-white?style=for-the-badge) |[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gabrielburgos1778@gmail.com) | [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GabyBoom)|
|Gianna giavarini|![](https://img.shields.io/badge/Base%20de%20Datos-yellow?style=for-the-badge) |[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:giannagiavarini@outlook.com) | [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/giannagiava)|
|Herman Aguilar|![](https://img.shields.io/badge/Programación-blue?style=for-the-badge) |[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:francogonzaloarce@gmail.com) | [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Franco-Arce)|
|Magali Bechis|![](https://img.shields.io/badge/Ética-white?style=for-the-badge) |[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:magalibechis3@gmail.com) | [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MagaBechis)|
|Erica Fernandez|![](https://img.shields.io/badge/Ética-white?style=for-the-badge) |[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ericave1919@gmail.com) | [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/EricaFerArg)|

<h2 align='center' >📕 Accede a los trabajos realizados</h2>

<h3 align='center' >▶ <a href="https://github.com/Winnie-The-POO-ARGBroker/ARGBroker-Demo/wiki" align='center'>Wiki </a></h3>



</div>
<br>

