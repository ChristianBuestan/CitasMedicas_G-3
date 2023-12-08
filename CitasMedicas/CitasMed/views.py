# En views.py
from rest_framework import generics
from .models import Usuario, PerfilAcceso, Reporte, MedicoPersonal, Paciente, ConsultaMedica, Facturacion, PlanCuentas, IntegracionContable, PrescripcionOrdenMedica, Certificado
from .serializers import UsuarioSerializer, PerfilAccesoSerializer, ReporteSerializer, MedicoPersonalSerializer, PacienteSerializer, ConsultaMedicaSerializer, FacturacionSerializer, PlanCuentasSerializer, IntegracionContableSerializer, PrescripcionOrdenMedicaSerializer, CertificadoSerializer


#CRUD usuarios-----------------------------------------------------------------------------
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


#CRUD perfil_acceso-----------------------------------------------------------------------------
class PerfilAccesoListCreateView(generics.ListCreateAPIView):
    queryset = PerfilAcceso.objects.all()
    serializer_class = PerfilAccesoSerializer

class PerfilAccesoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerfilAcceso.objects.all()
    serializer_class = PerfilAccesoSerializer


#CRUD reporte-----------------------------------------------------------------------------
class ReporteListCreateView(generics.ListCreateAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class ReporteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer


#CRUD medico_personal-----------------------------------------------------------------------------
class MedicoPersonalListCreateView(generics.ListCreateAPIView):
    queryset = MedicoPersonal.objects.all()
    serializer_class = MedicoPersonalSerializer

class MedicoPersonalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicoPersonal.objects.all()
    serializer_class = MedicoPersonalSerializer


#CRUD paciente-----------------------------------------------------------------------------
class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


#CRUD consulta_medica-----------------------------------------------------------------------------
class ConsultaMedicaListCreateView(generics.ListCreateAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class ConsultaMedicaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer


#CRUD facturacion-----------------------------------------------------------------------------
class FacturacionListCreateView(generics.ListCreateAPIView):
    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer

class FacturacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer


#CRUD plan_cuentas-----------------------------------------------------------------------------
class PlanCuentasListCreateView(generics.ListCreateAPIView):
    queryset = PlanCuentas.objects.all()
    serializer_class = PlanCuentasSerializer

class PlanCuentasDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlanCuentas.objects.all()
    serializer_class = PlanCuentasSerializer


#CRUD integracion_contable-----------------------------------------------------------------------------
class IntegracionContableListCreateView(generics.ListCreateAPIView):
    queryset = IntegracionContable.objects.all()
    serializer_class = IntegracionContableSerializer

class IntegracionContableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IntegracionContable.objects.all()
    serializer_class = IntegracionContableSerializer


#CRUD prescripcion_orden_medica-----------------------------------------------------------------------------
class PrescripcionOrdenMedicaListCreateView(generics.ListCreateAPIView):
    queryset = PrescripcionOrdenMedica.objects.all()
    serializer_class = PrescripcionOrdenMedicaSerializer

class PrescripcionOrdenMedicaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrescripcionOrdenMedica.objects.all()
    serializer_class = PrescripcionOrdenMedicaSerializer


#CRUD certificado-----------------------------------------------------------------------------
class CertificadoListCreateView(generics.ListCreateAPIView):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer

class CertificadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer