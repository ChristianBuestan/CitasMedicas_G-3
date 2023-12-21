import os
import django

# Reemplaza 'myproject.settings' con la ruta de tu archivo settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CitasMedicas.settings')
django.setup()

# En views.py

from django.test import TestCase
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework import generics
from django.test import RequestFactory
from CitasMed.models import Usuario, PerfilAcceso, Reporte, MedicoPersonal, Paciente, ConsultaMedica, Facturacion, PlanCuentas, IntegracionContable, PrescripcionOrdenMedica, Certificado
from CitasMed.serializers import UsuarioSerializer, PerfilAccesoSerializer, ReporteSerializer, MedicoPersonalSerializer, PacienteSerializer, ConsultaMedicaSerializer, FacturacionSerializer, PlanCuentasSerializer, IntegracionContableSerializer, PrescripcionOrdenMedicaSerializer, CertificadoSerializer


#CRUD usuarios-----------------------------------------------------------------------------
class UsuarioListCreateView(generics.ListCreateAPIView):  
    
    """
    Esta vista maneja la lista y creación de usuarios.

    Aquí un ejemplo de cómo se puede probar la creación de un usuario:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import UsuarioListCreateView

    # Creamos una fábrica de peticiones y una petición POST con datos de usuario
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('usuario-list-create'), 
    ... {'usu_cedula': '1234567890', 'usu_nombre_completo': 'Juan Pérez', 
    ... 'usu_numero_telefono': '123456789', 'usu_correo_electronico': 'juan@example.com', 
    ... 'usu_direccion': 'Calle 123'}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = UsuarioListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que el usuario se haya creado con éxito
    >>> response.status_code == 201
    >>> response.data

    True
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# CRUD PerfilAccesoListCreateView-----------------------------------------------------------------------------
class PerfilAccesoListCreateView(generics.ListCreateAPIView):

    """
    Esta vista maneja la lista y creación de perfiles de acceso.

    Aquí un ejemplo de cómo se puede probar la creación de un perfil de acceso:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import PerfilAccesoListCreateView
    >>> from .models import Usuario

    # Primero, necesitamos crear un usuario para asociar con el perfil de acceso
    >>> usuario = Usuario.objects.create(
    ...     usu_cedula='1234567890',
    ...     usu_nombre_completo='Juan Pérez',
    ...     usu_numero_telefono='123456789',
    ...     usu_correo_electronico='juan@example.com',
    ...     usu_direccion='Calle 123'
    ... )

    # Creamos una fábrica de peticiones y una petición POST con datos del perfil de acceso
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('perfilacceso-list-create'), 
    ... {'perf_acc_nivel_acceso': 'Nivel 1', 'usuario': usuario.id}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = PerfilAccesoListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que el perfil de acceso se haya creado con éxito
    >>> response.status_code == 201
    True
    """


    queryset = PerfilAcceso.objects.all()
    serializer_class = PerfilAccesoSerializer

class PerfilAccesoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerfilAcceso.objects.all()
    serializer_class = PerfilAccesoSerializer


# CRUD ReporteListCreateView-----------------------------------------------------------------------------
class ReporteListCreateView(generics.ListCreateAPIView):

    """
    Esta vista maneja la lista y creación de reportes.

    Aquí un ejemplo de cómo se puede probar la creación de un reporte:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import ReporteListCreateView
    >>> from .models import Reporte, Usuario

    # Primero, necesitamos crear un usuario para asociar con el reporte
    >>> usuario = Usuario.objects.create(
    ...     usu_cedula='1234567890',
    ...     usu_nombre_completo='Juan Pérez',
    ...     usu_numero_telefono='123456789',
    ...     usu_correo_electronico='juan@example.com',
    ...     usu_direccion='Calle 123'
    ... )

    # Creamos una fábrica de peticiones y una petición POST con datos del reporte
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('reporte-list-create'), 
    ... {'rep_tipo_reporte': 'Tipo 1', 'rep_parametros': 'Parametros del reporte', 'usuario': usuario.id}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = ReporteListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que el reporte se haya creado con éxito
    >>> response.status_code == 201
    True
    """

    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class ReporteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer


# CRUD MedicoPersonalListCreateView-----------------------------------------------------------------------------
class MedicoPersonalListCreateView(generics.ListCreateAPIView):

    """
    Esta vista maneja la lista y creación de personal médico.

    Aquí un ejemplo de cómo se puede probar la creación de un registro de personal médico:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import MedicoPersonalListCreateView
    >>> from .models import MedicoPersonal, Reporte, Usuario

    # Primero, necesitamos crear un usuario y un reporte para asociar con el personal médico
    >>> usuario = Usuario.objects.create(
    ...     usu_cedula='1234567890',
    ...     usu_nombre_completo='Juan Pérez',
    ...     usu_numero_telefono='123456789',
    ...     usu_correo_electronico='juan@example.com',
    ...     usu_direccion='Calle 123'
    ... )
    >>> reporte = Reporte.objects.create(
    ...     rep_tipo_reporte='Tipo 1',
    ...     rep_parametros='Parametros del reporte',
    ...     usuario=usuario
    ... )

    # Creamos una fábrica de peticiones y una petición POST con datos del personal médico
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('medicopersonal-list-create'), 
    ... {'med_per_nombre_completo': 'Dr. Ana Torres', 'med_per_credenciales': 'Credenciales del médico', 
    ... 'med_per_especialidades': 'Especialidad 1, Especialidad 2', 'med_per_horarios_consulta': 'Lunes a Viernes 9am - 5pm', 
    ... 'med_per_informacion_contacto': 'info@contacto.com', 'reportes': reporte.id}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = MedicoPersonalListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que el registro de personal médico se haya creado con éxito
    >>> response.status_code == 201
    True
    """

    queryset = MedicoPersonal.objects.all()
    serializer_class = MedicoPersonalSerializer


class MedicoPersonalDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = MedicoPersonal.objects.all()
    serializer_class = MedicoPersonalSerializer


# CRUD PacienteListCreateView-----------------------------------------------------------------------------
class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    """
    Esta vista maneja la lista y creación de pacientes.

    Aquí un ejemplo de cómo se puede probar la creación de un registro de paciente:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import PacienteListCreateView
    >>> from .models import Paciente, MedicoPersonal, Reporte, Usuario
    >>> from django.utils import timezone

    # Primero, necesitamos crear un usuario, un reporte y un médico personal para asociar con el paciente
    >>> usuario = Usuario.objects.create(
    ...     usu_cedula='1234567890',
    ...     usu_nombre_completo='Juan Pérez',
    ...     usu_numero_telefono='123456789',
    ...     usu_correo_electronico='juan@example.com',
    ...     usu_direccion='Calle 123'
    ... )
    >>> reporte = Reporte.objects.create(
    ...     rep_tipo_reporte='Tipo 1',
    ...     rep_parametros='Parametros del reporte',
    ...     usuario=usuario
    ... )
    >>> medico_personal = MedicoPersonal.objects.create(
    ...     med_per_nombre_completo='Dr. Ana Torres',
    ...     med_per_credenciales='Credenciales del médico',
    ...     med_per_especialidades='Especialidad 1, Especialidad 2',
    ...     med_per_horarios_consulta='Lunes a Viernes 9am - 5pm',
    ...     med_per_informacion_contacto='info@contacto.com',
    ...     reportes=reporte
    ... )

    # Creamos una fábrica de peticiones y una petición POST con datos del paciente
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('paciente-list-create'), 
    ... {'pac_nombre_completo': 'María López', 'pac_fecha_nacimiento': str(timezone.now().date()), 
    ... 'pac_genero': 'Femenino', 'pac_direccion': 'Calle 456', 'pac_numero_telefono': '987654321', 
    ... 'pac_correo_electronico': 'maria@example.com', 'pac_antecedentes_medicos': '', 'pac_enfermedades': '', 
    ... 'pac_alergias': '', 'pac_medicamentos_actuales': '', 'medico_personal': medico_personal.id}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = PacienteListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que el registro de paciente se haya creado con éxito
    >>> response.status_code == 201
    True
    """




class PacienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


# CRUD ConsultaMedicaListCreateView-----------------------------------------------------------------------------
class ConsultaMedicaListCreateView(generics.ListCreateAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

    """
    Esta vista maneja la lista y creación de consultas médicas.

    Aquí un ejemplo de cómo se puede probar la creación de una consulta médica:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import ConsultaMedicaListCreateView
    >>> from .models import ConsultaMedica, MedicoPersonal, Paciente, Reporte, Usuario

    # Primero, necesitamos crear las entidades requeridas: Usuario, Reporte, MedicoPersonal, y Paciente
    >>> usuario = Usuario.objects.create(
    ...     usu_cedula='1234567890',
    ...     usu_nombre_completo='Juan Pérez',
    ...     usu_numero_telefono='123456789',
    ...     usu_correo_electronico='juan@example.com',
    ...     usu_direccion='Calle 123'
    ... )
    >>> reporte = Reporte.objects.create(
    ...     rep_tipo_reporte='Tipo 1',
    ...     rep_parametros='Parametros del reporte',
    ...     usuario=usuario
    ... )
    >>> medico_personal = MedicoPersonal.objects.create(
    ...     med_per_nombre_completo='Dr. Ana Torres',
    ...     med_per_credenciales='Credenciales del médico',
    ...     med_per_especialidades='Especialidad 1, Especialidad 2',
    ...     med_per_horarios_consulta='Lunes a Viernes 9am - 5pm',
    ...     med_per_informacion_contacto='info@contacto.com',
    ...     reportes=reporte
    ... )
    >>> paciente = Paciente.objects.create(
    ...     pac_nombre_completo='María López',
    ...     pac_fecha_nacimiento='2000-01-01',
    ...     pac_genero='Femenino',
    ...     pac_direccion='Calle 456',
    ...     pac_numero_telefono='987654321',
    ...     pac_correo_electronico='maria@example.com',
    ...     pac_antecedentes_medicos='',
    ...     pac_enfermedades='',
    ...     pac_alergias='',
    ...     pac_medicamentos_actuales='',
    ...     medico_personal=medico_personal
    ... )

    # Creamos una fábrica de peticiones y una petición POST con datos de la consulta médica
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('consultamedica-list-create'), 
    ... {'con_med_medico_personal': medico_personal.id, 'con_med_paciente': paciente.id, 
    ... 'con_med_diagnostico': 'Diagnostico de ejemplo', 'con_med_recomendaciones': 'Recomendaciones de ejemplo'}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = ConsultaMedicaListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que la consulta médica se haya creado con éxito
    >>> response.status_code == 201
    True
    """



class ConsultaMedicaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer


# CRUD FacturacionListCreateView-----------------------------------------------------------------------------
class FacturacionListCreateView(generics.ListCreateAPIView):
    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer

    """
    Esta vista maneja la lista y creación de facturaciones.

    Aquí un ejemplo de cómo se puede probar la creación de una facturación:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import FacturacionListCreateView
    >>> from .models import Facturacion, Paciente, MedicoPersonal, Reporte, Usuario
    >>> from django.utils import timezone

    # Primero, necesitamos crear las entidades requeridas: Usuario, Reporte, MedicoPersonal, y Paciente
    >>> usuario = Usuario.objects.create(
    ...     usu_cedula='1234567890',
    ...     usu_nombre_completo='Juan Pérez',
    ...     usu_numero_telefono='123456789',
    ...     usu_correo_electronico='juan@example.com',
    ...     usu_direccion='Calle 123'
    ... )
    >>> reporte = Reporte.objects.create(
    ...     rep_tipo_reporte='Tipo 1',
    ...     rep_parametros='Parametros del reporte',
    ...     usuario=usuario
    ... )
    >>> medico_personal = MedicoPersonal.objects.create(
    ...     med_per_nombre_completo='Dr. Ana Torres',
    ...     med_per_credenciales='Credenciales del médico',
    ...     med_per_especialidades='Especialidad 1, Especialidad 2',
    ...     med_per_horarios_consulta='Lunes a Viernes 9am - 5pm',
    ...     med_per_informacion_contacto='info@contacto.com',
    ...     reportes=reporte
    ... )
    >>> paciente = Paciente.objects.create(
    ...     pac_nombre_completo='María López',
    ...     pac_fecha_nacimiento='2000-01-01',
    ...     pac_genero='Femenino',
    ...     pac_direccion='Calle 456',
    ...     pac_numero_telefono='987654321',
    ...     pac_correo_electronico='maria@example.com',
    ...     pac_antecedentes_medicos='',
    ...     pac_enfermedades='',
    ...     pac_alergias='',
    ...     pac_medicamentos_actuales='',
    ...     medico_personal=medico_personal
    ... )

    # Creamos una fábrica de peticiones y una petición POST con datos de la facturación
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('facturacion-list-create'), 
    ... {'fact_nombre_paciente': 'María López', 'fact_numero_identificacion': '987654321', 
    ... 'fact_numero_poliza_seguro': '12345', 'fact_detalles_facturacion': 'Detalles de la facturación', 
    ... 'fact_estado_pago': 'Pendiente', 'fact_metodo_pago': 'Tarjeta de crédito', 'paciente': paciente.id}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = FacturacionListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que la facturación se haya creado con éxito
    >>> response.status_code == 201
    True
    """


class FacturacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer


# CRUD PlanCuentasListCreateView-----------------------------------------------------------------------------
class PlanCuentasListCreateView(generics.ListCreateAPIView):

    """
    Esta vista maneja la lista y creación de planes de cuentas.

    Aquí un ejemplo de cómo se puede probar la creación de un plan de cuentas:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import PlanCuentasListCreateView
    >>> from .models import PlanCuentas, ConsultaMedica, MedicoPersonal, Paciente, Reporte, Usuario
    >>> from django.utils import timezone

    # Primero, necesitamos crear las entidades requeridas para una consulta médica
    >>> usuario = Usuario.objects.create(
    ...     usu_cedula='1234567890',
    ...     usu_nombre_completo='Juan Pérez',
    ...     usu_numero_telefono='123456789',
    ...     usu_correo_electronico='juan@example.com',
    ...     usu_direccion='Calle 123'
    ... )
    >>> reporte = Reporte.objects.create(
    ...     rep_tipo_reporte='Tipo 1',
    ...     rep_parametros='Parametros del reporte',
    ...     usuario=usuario
    ... )
    >>> medico_personal = MedicoPersonal.objects.create(
    ...     med_per_nombre_completo='Dr. Ana Torres',
    ...     med_per_credenciales='Credenciales del médico',
    ...     med_per_especialidades='Especialidad 1, Especialidad 2',
    ...     med_per_horarios_consulta='Lunes a Viernes 9am - 5pm',
    ...     med_per_informacion_contacto='info@contacto.com',
    ...     reportes=reporte
    ... )
    >>> paciente = Paciente.objects.create(
    ...     pac_nombre_completo='María López',
    ...     pac_fecha_nacimiento='2000-01-01',
    ...     pac_genero='Femenino',
    ...     pac_direccion='Calle 456',
    ...     pac_numero_telefono='987654321',
    ...     pac_correo_electronico='maria@example.com',
    ...     pac_antecedentes_medicos='',
    ...     pac_enfermedades='',
    ...     pac_alergias='',
    ...     pac_medicamentos_actuales='',
    ...     medico_personal=medico_personal
    ... )
    >>> consulta_medica = ConsultaMedica.objects.create(
    ...     con_med_medico_personal=medico_personal,
    ...     con_med_paciente=paciente,
    ...     con_med_diagnostico='Diagnostico de ejemplo',
    ...     con_med_recomendaciones='Recomendaciones de ejemplo'
    ... )

    # Creamos una fábrica de peticiones y una petición POST con datos del plan de cuentas
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('plancuentas-list-create'), 
    ... {'plan_cue_fecha_transaccion': str(timezone.now().date()), 'plan_cue_tipo_transaccion': 'Tipo de transacción', 
    ... 'plan_cue_monto': '100.00', 'plan_cue_descripcion': 'Descripción del plan de cuentas', 
    ... 'plan_cue_numero_referencia': '123456', 'plan_cue_cuenta_destino': 'Cuenta destino', 
    ... 'plan_cue_metodo_pago': 'Método de pago', 'plan_cue_categoria_gasto_ingreso': 'Categoría del gasto', 
    ... 'plan_cue_datos_proveedor_cliente': 'Datos del proveedor o cliente', 'consulta_medica': consulta_medica.id}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = PlanCuentasListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que el plan de cuentas se haya creado con éxito
    >>> response.status_code == 201
    True
    """

    queryset = PlanCuentas.objects.all()
    serializer_class = PlanCuentasSerializer


class PlanCuentasDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PlanCuentas.objects.all()
    serializer_class = PlanCuentasSerializer


# CRUD IntegracionContableListCreateView-----------------------------------------------------------------------------
class IntegracionContableListCreateView(generics.ListCreateAPIView):

    """
    Esta vista maneja la lista y creación de integraciones contables.

    Aquí un ejemplo de cómo se puede probar la creación de una integración contable:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import IntegracionContableListCreateView
    >>> from .models import IntegracionContable, PlanCuentas, ConsultaMedica, MedicoPersonal, Paciente, Reporte, Usuario
    >>> from django.utils import timezone

    # Primero, necesitamos crear todas las entidades requeridas para crear un PlanCuentas
    >>> usuario = Usuario.objects.create(
    ...     usu_cedula='1234567890',
    ...     usu_nombre_completo='Juan Pérez',
    ...     usu_numero_telefono='123456789',
    ...     usu_correo_electronico='juan@example.com',
    ...     usu_direccion='Calle 123'
    ... )
    >>> reporte = Reporte.objects.create(
    ...     rep_tipo_reporte='Tipo 1',
    ...     rep_parametros='Parametros del reporte',
    ...     usuario=usuario
    ... )
    >>> medico_personal = MedicoPersonal.objects.create(
    ...     med_per_nombre_completo='Dr. Ana Torres',
    ...     med_per_credenciales='Credenciales del médico',
    ...     med_per_especialidades='Especialidad 1, Especialidad 2',
    ...     med_per_horarios_consulta='Lunes a Viernes 9am - 5pm',
    ...     med_per_informacion_contacto='info@contacto.com',
    ...     reportes=reporte
    ... )
    >>> paciente = Paciente.objects.create(
    ...     pac_nombre_completo='María López',
    ...     pac_fecha_nacimiento='2000-01-01',
    ...     pac_genero='Femenino',
    ...     pac_direccion='Calle 456',
    ...     pac_numero_telefono='987654321',
    ...     pac_correo_electronico='maria@example.com',
    ...     pac_antecedentes_medicos='',
    ...     pac_enfermedades='',
    ...     pac_alergias='',
    ...     pac_medicamentos_actuales='',
    ...     medico_personal=medico_personal
    ... )
    >>> consulta_medica = ConsultaMedica.objects.create(
    ...     con_med_medico_personal=medico_personal,
    ...     con_med_paciente=paciente,
    ...     con_med_diagnostico='Diagnostico de ejemplo',
    ...     con_med_recomendaciones='Recomendaciones de ejemplo'
    ... )
    >>> plan_cuentas = PlanCuentas.objects.create(
    ...     plan_cue_fecha_transaccion=timezone.now(),
    ...     plan_cue_tipo_transaccion='Tipo de transacción',
    ...     plan_cue_monto=100.00,
    ...     plan_cue_descripcion='Descripción del plan de cuentas',
    ...     plan_cue_numero_referencia='123456',
    ...     plan_cue_cuenta_destino='Cuenta destino',
    ...     plan_cue_metodo_pago='Método de pago',
    ...     plan_cue_categoria_gasto_ingreso='Categoría del gasto',
    ...     plan_cue_datos_proveedor_cliente='Datos del proveedor o cliente',
    ...     consulta_medica=consulta_medica
    ... )

    # Creamos una fábrica de peticiones y una petición POST con datos de la integración contable
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('integracioncontable-list-create'), 
    ... {'integ_cont_datos_financieros': 'Datos financieros de ejemplo', 'plan_cuentas': plan_cuentas.id}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = IntegracionContableListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que la integración contable se haya creado con éxito
    >>> response.status_code == 201
    True
    """

    queryset = IntegracionContable.objects.all()
    serializer_class = IntegracionContableSerializer


class IntegracionContableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IntegracionContable.objects.all()
    serializer_class = IntegracionContableSerializer


# CRUD PrescripcionOrdenMedicaListCreateView-----------------------------------------------------------------------------
class PrescripcionOrdenMedicaListCreateView(generics.ListCreateAPIView):

    """
    Esta vista maneja la lista y creación de prescripciones de órdenes médicas.

    Aquí un ejemplo de cómo se puede probar la creación de una prescripción de orden médica:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import PrescripcionOrdenMedicaListCreateView
    >>> from .models import PrescripcionOrdenMedica, ConsultaMedica, MedicoPersonal, Paciente, Reporte, Usuario
    >>> from django.utils import timezone

    # Primero, necesitamos crear todas las entidades requeridas para una ConsultaMedica
    >>> usuario = Usuario.objects.create(
    ...     usu_cedula='1234567890',
    ...     usu_nombre_completo='Juan Pérez',
    ...     usu_numero_telefono='123456789',
    ...     usu_correo_electronico='juan@example.com',
    ...     usu_direccion='Calle 123'
    ... )
    >>> reporte = Reporte.objects.create(
    ...     rep_tipo_reporte='Tipo 1',
    ...     rep_parametros='Parametros del reporte',
    ...     usuario=usuario
    ... )
    >>> medico_personal = MedicoPersonal.objects.create(
    ...     med_per_nombre_completo='Dr. Ana Torres',
    ...     med_per_credenciales='Credenciales del médico',
    ...     med_per_especialidades='Especialidad 1, Especialidad 2',
    ...     med_per_horarios_consulta='Lunes a Viernes 9am - 5pm',
    ...     med_per_informacion_contacto='info@contacto.com',
    ...     reportes=reporte
    ... )
    >>> paciente = Paciente.objects.create(
    ...     pac_nombre_completo='María López',
    ...     pac_fecha_nacimiento='2000-01-01',
    ...     pac_genero='Femenino',
    ...     pac_direccion='Calle 456',
    ...     pac_numero_telefono='987654321',
    ...     pac_correo_electronico='maria@example.com',
    ...     pac_antecedentes_medicos='',
    ...     pac_enfermedades='',
    ...     pac_alergias='',
    ...     pac_medicamentos_actuales='',
    ...     medico_personal=medico_personal
    ... )
    >>> consulta_medica = ConsultaMedica.objects.create(
    ...     con_med_medico_personal=medico_personal,
    ...     con_med_paciente=paciente,
    ...     con_med_diagnostico='Diagnostico de ejemplo',
    ...     con_med_recomendaciones='Recomendaciones de ejemplo'
    ... )

    # Creamos una fábrica de peticiones y una petición POST con datos de la prescripción de orden médica
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('prescripcionordenmedica-list-create'), 
    ... {'pres_ord_nombre_paciente': 'María López', 'pres_ord_fecha_emision': str(timezone.now().date()), 
    ... 'pres_ord_detalles_prescripcion': 'Detalles de la prescripción', 'pres_ord_estado_cumplimiento': 'Pendiente', 
    ... 'consulta_medica': consulta_medica.id}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = PrescripcionOrdenMedicaListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que la prescripción de orden médica se haya creado con éxito
    >>> response.status_code == 201
    True
    """

    queryset = PrescripcionOrdenMedica.objects.all()
    serializer_class = PrescripcionOrdenMedicaSerializer


class PrescripcionOrdenMedicaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrescripcionOrdenMedica.objects.all()
    serializer_class = PrescripcionOrdenMedicaSerializer


# CRUD CertificadoListCreateView-----------------------------------------------------------------------------
class CertificadoListCreateView(generics.ListCreateAPIView):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer

    """
    Esta vista maneja la lista y creación de certificados.

    Aquí un ejemplo de cómo se puede probar la creación de un certificado:

    >>> from rest_framework.test import APIRequestFactory
    >>> from django.urls import reverse
    >>> from .views import CertificadoListCreateView
    >>> from .models import Certificado
    >>> from django.utils import timezone

    # Creamos una fábrica de peticiones y una petición POST con datos del certificado
    >>> factory = APIRequestFactory()
    >>> request = factory.post(reverse('certificado-list-create'), 
    ... {'cert_titulo': 'Certificado de Excelencia', 'cert_emisor': 'Universidad X', 
    ... 'cert_receptor': 'Juan Pérez', 'cert_fecha_emision': str(timezone.now().date()), 
    ... 'cert_descripcion': 'Certificado otorgado por logros académicos excepcionales'}, format='json')

    # Ahora, creamos una instancia de la vista y la procesamos con la petición
    >>> view = CertificadoListCreateView.as_view()
    >>> response = view(request)

    # Verificamos que el certificado se haya creado con éxito
    >>> response.status_code == 201
    True
    """


class CertificadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer