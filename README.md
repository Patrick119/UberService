# Proyecto UberService

## Descripción del Proyecto

El proyecto UberService es una plataforma desarrollada en Django para la gestión de profesionales y servicios. El objetivo principal de esta aplicación es conectar a profesionales de diversas áreas con usuarios que requieren servicios específicos. La plataforma permite a los usuarios solicitar servicios, recibir ofertas de profesionales, realizar pagos y dejar reseñas.

## Integrantes del Equipo

- Pou
- Pollo
- Rata
- Wazouski

## Funcionalidades Principales

### 1. Gestión de Profesiones
Permite la creación y administración de diferentes profesiones, incluyendo su nombre y descripción.

### 2. Gestión de Profesionales
Los profesionales pueden registrarse en la plataforma, especificar su profesión, experiencia, tarifa por hora y ubicación.

### 3. Servicios
Los profesionales pueden crear y administrar servicios que ofrecen, incluyendo la descripción detallada y las tarifas correspondientes.

### 4. Solicitudes de Servicios
Los usuarios pueden crear solicitudes de servicios, especificando la profesión requerida, una descripción del trabajo, la ubicación y el presupuesto ofrecido.

### 5. Ofertas de Profesionales
Los profesionales pueden responder a las solicitudes de servicios con ofertas personalizadas, incluyendo el precio y la descripción del servicio ofrecido.

### 6. Órdenes de Servicio
Una vez aceptada una oferta, se genera una orden de servicio que incluye la información detallada del servicio, las fechas de inicio y fin, y el estado del servicio.

### 7. Reseñas y Calificaciones
Los usuarios pueden dejar reseñas y calificaciones sobre los servicios recibidos, lo cual ayuda a mantener un sistema de retroalimentación y reputación para los profesionales.

### 8. Pagos
Integración de métodos de pago para gestionar las transacciones entre usuarios y profesionales, incluyendo detalles de transacción y estado del pago.

### 9. Direcciones y Disponibilidad
Gestión de direcciones de los usuarios y la disponibilidad horaria de los profesionales.

### 10. Sistema de Puntos y Recompensas
Los usuarios pueden acumular puntos por diversas actividades y canjearlos por recompensas.

### 11. Ajustes de Tarifas y Desafíos
Administración de tarifas mínimas y máximas para cada profesión, y la posibilidad de crear desafíos con recompensas para los profesionales.

## Estructura del Proyecto

La aplicación está dividida en varios modelos para manejar las diferentes entidades del sistema. Estos incluyen:

- **Profesion**: Maneja las diferentes profesiones disponibles en la plataforma.
- **Profesional**: Información sobre los profesionales registrados.
- **Servicio**: Servicios ofrecidos por los profesionales.
- **ImagenServicio**: Imágenes asociadas a los servicios.
- **SolicitudServicio**: Solicitudes de servicios creadas por los usuarios.
- **Oferta**: Ofertas hechas por los profesionales en respuesta a las solicitudes de servicio.
- **OrdenServicio**: Detalles de las órdenes de servicio generadas.
- **Reseña**: Reseñas y calificaciones de los servicios.
- **Pago**: Gestión de pagos y transacciones.
- **Direccion**: Direcciones de los usuarios.
- **DisponibilidadProfesional**: Horarios de disponibilidad de los profesionales.
- **MetodoPagoUsuario**: Métodos de pago registrados por los usuarios.
- **ResumenReseñasProfesional**: Resumen de las reseñas y calificaciones de los profesionales.
- **AjusteTarifa**: Configuración de tarifas para las profesiones.
- **Puntos**: Sistema de puntos para los usuarios.
- **Recompensa**: Recompensas disponibles para canje.
- **Desafio**: Desafíos creados para los profesionales.

## Instalación y Configuración

### Requisitos

- Python 3.x
- Django 3.x
- PostGIS (para manejar datos geoespaciales)
- Virtualenv (recomendado)

### Pasos para la Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv my_env
    source my_env/bin/activate   # En Windows usa: my_env\Scripts\activate

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt

5. Configura las variables de entorno:
    ```bash
    set DJANGO_SETTINGS_MODULE=mywebapp.settings  # En Windows
    export DJANGO_SETTINGS_MODULE=mywebapp.settings  # En Linux/Mac

6. Realiza las migraciones y corre el servidor:
    ```bash
    python manage.py migrate
    python manage.py runserver

## Uso de la Aplicación
### Crear Datos Iniciales
Para crear datos iniciales en la base de datos, ejecuta el script datos_iniciales.py:
    ```bash
    
    python datos_iniciales.py
    Acceso a la Aplicación
    Abre tu navegador y navega a http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.
