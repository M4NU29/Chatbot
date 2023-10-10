
# Emmanuel Espinal
# 2022-0038

from ChatBot import ChatBot

responses = [
    {
        'bot_response': 'Hola, ¿En qué puedo ayudarte?',
        'list_of_words': ['hola', 'saludos', 'tal', 'buenas'],
        'single_response': True
    },
    {
        'bot_response': 'Dime si necesitas ayuda con algo más.',
        'list_of_words': ['gracias', 'agradezco', 'thank', 'thanks'],
        'single_response': True
    },
    {
        'bot_response': 'Actualmente ofrecemos las carreras de:\n\t· Simulaciones Interactivas y Videojuegos\n\t· Telecomunicaciones\n\t· Inteligencia Artificial\n\t· Informática Forense\n\t· Energías Renovables\n\t· Redes de la Información\n\t· Mecatrónica\n\t· Manufactura Automatizada\n\t· Manufactura de Dispositivos Médicos\n\t· Diseño Industrial\n\t· Multimedia\n\t· Sonido\n\t· Desarrollo de Software\n\t· Analítica y Ciencia de los datos\n\t· Seguridad Informática\n\tPara más información puedes acceder a https://itla.edu.do/carreras-tecnologicas/',
        'list_of_words': ['cuales', 'que', 'carreras', 'tecnologos', 'programas', 'estudios', 'oferta academica']
    },
    {
        'bot_response': 'El proceso de admisión consta de 5 sencillos pasos:\n\t1. Debes realizar la solicitud de admisión a través de nuestro portal web.\n\t2. Debes realizar el pago por derecho a admisión de RD$500.00\n\t3. Procede a adjuntar los documentos digitalizados en la plataforma ORBI.\n\t4. Entrega los documentos en original al departamento de Admisiones.\n\t5. Toma los exámenes de admisión, nivel de inglés y propedéutico de matemáticas en la fecha correspondiente.\n\tSi quieres saber más, en https://itla.edu.do/admisiones/ está toda la información que necesitas.',
        'list_of_words': ['admision', 'admisiones', 'proceso', 'pasos', 'solicitud', 'ingresar']
    },
    {
        'bot_response': 'Los requisitos básicos para aplicar al programa de Becas de Excelencia son:\n\t· Ser admitido por la institución.\n\t· Tener un promedio de mínimo 90 ptos.\n\t· Ser dominicano y/o de nacionalidad dominicana.\n\t· Hacer la solicitud en la fecha indicada a través de ORBI.\n\t· Obtener 600 puntos o más en la prueba POMA.\n\tPara más detalles accede a https://itla.edu.do/becas-y-financiamiento/',
        'list_of_words': ['beca', 'becas', 'excelencia']
    },
    {
        'bot_response': 'Estamos ubicados en la Autopista Las Américas, Km. 27, PCSD, La Caleta, Boca Chica 11606.',
        'list_of_words': ['ubicacion', 'ubicados', 'direccion', 'donde estan', 'encuentran']
    },
    {
        'bot_response': 'Para solicitar una constancia de estudios, debes pasar por el departamento de registro. La constancia tiene un costo de RD$100.00',
        'list_of_words': ['constancia', 'estudio', 'estudios'],
        'required_words': ['constancia']
    },
    {
        'bot_response': 'Para reservar tu ticket de transporte debes seguir los siguientes pasos:\n\t1. Ingresar a la página web transporte.itla.edu.do\n\t2. Realizar la solicitud de ticket.\n\t3. Reservar los tickets solicitados.\n\t4. Imprimir los tickets en el área de impresión, en el BookShop del Edificio 4 de ITLA.\n\t5. Entregar el ticket de reservación a la hora de abordar el autobús.\n\tRecuerda que debes reservar tus tickets 24 horas antes; en caso de que necesites más información puedes acceder a https://itla.edu.do/transporte/',
        'list_of_words': ['transporte', 'ticket', 'tickets', 'reservar'],
        'required_words': ['transporte']
    },
    {
        'bot_response': 'Siempre puedes ir a la biblioteca Prof. Erich Kunhardt en el edificio 4 de ITLA. También recuerda que con tu correo institucional obtienes acceso a las bibliotecas virtuales de EBSCO y OReilly. Si te interesa saber más puedes acceder a https://itla.edu.do/biblioteca/',
        'list_of_words': ['biblioteca', 'recursos', 'libros', 'libro']
    },
    {
        'bot_response': 'Puedes visitarnos de lunes a viernes de 8:00 am a 10:00 pm y sábados de 9:00 am a 6:00 pm.',
        'list_of_words': ['horario', 'cuando', 'visitar', 'hora', 'abierto', 'abiertos']
    },
    {
        'bot_response': 'Puedes contactar con nosotros a través de los teléfonos (809) 738-4852 / (809) 793-2557 o a través del correo info@itla.edu.do',
        'list_of_words': ['contacto', 'telefono', 'correo', 'info', 'informacion', 'hablar', 'llamar', 'comunicar']
    },
    {
        'bot_response': 'En promedio nuestros tecnólogos tienen una duración de 2 años y 4 meses.',
        'list_of_words': ['duracion', 'duran', 'tiempo', 'cuanto', 'tecnologos', 'carreras', 'carrera']
    }
]

bot = ChatBot(responses)

while True:
    print("Bot: " + bot.get_response(input('You: ')))
