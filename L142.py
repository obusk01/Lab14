#Bethany B, Grace A, Olivia B
class Ambulance:
    """Represents an ambulance

    attributes:color, siren, height, patient."""


def patient(Amb):
    if Amb.patient>0:
        speed=2.3*(Amb.patient-0.5)*Amb.traffic+30*(Amb.patient-2.143)
        return speed
    else:
        return Amb.traffic

a=Ambulance()
a.color="red"
a.siren="loud"
a.height=30
a.patient=10
a.traffic=20

print(patient(a))
