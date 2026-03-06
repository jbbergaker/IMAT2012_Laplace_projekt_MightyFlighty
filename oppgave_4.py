import scipy . signal as sig
import matplotlib.pyplot as plt
import numpy as np

#deloppgave a

w=np.logspace(-2, 2, 1000)
t = np.linspace (0 , 0.02 , 501) # Tidsvindu for simulering
v_inn = np.sin (500* t ) # P ˚a trykt spenning v_inn ( t )
system = sig.TransferFunction ([0, 2000**2] , [1 , 2*0.5*2000 , 2000**2]) # Eksempel på transferfunksjon
_ , v_ut , _ = sig.lsim ( system , U = v_inn , T = t ) # Beregn utgangsspenningen 'v_ut ' gitt p ˚a trykt spenning ' v_inn ' for kretsen representert med 'system

#Finner to punkter for å regne ut tidsforskyvning
for i in range(500):
    if -0.01<v_inn[i]<0.01:
        print(f'Tidspunkt fra v_inn: {t[i]}')
    if -0.01<v_ut[i]<0.01:
        print(f'Tidspunkt fra v_ut: {t[i]}')

#Finner amplitude
amplitude_v_inn = (np.max(v_inn)-np.min(v_inn))/2
amplitude_v_ut = (np.max(v_ut[400:500])-np.min(v_ut[400:500]))/2
print(f'Amplitude til v_inn: {amplitude_v_inn}')
print(f'Amplitude til v_ut: {amplitude_v_ut}')


# #Faseforskyvning regnes ut for hånd

#Plotter v_inn og v_ut
plt.plot(t, v_inn, label="v0(t)")
plt.plot(t, v_ut, label="vC(t)")
plt.legend()
plt.xlabel("Tid [s]")
plt.ylabel("Spenning")
plt.grid()
plt.show()

#endrer frekvensen i linje 9 for oppgave b

#deloppgave c

omega = np.array([500, 1000, 2000, 4000]) # frekvensene i rad/s 
frek, H = sig.freqresp(system, w=omega) #funksjon som gir tilbake frekvensene, og finner transferfunksjonen med komplexe tall
modulus = np.abs(H) #Finner lengden av den komplekse delen
argument = np.angle(H) #Finner argumentet i radianer

print("omega:", omega) 
print("|H(jω)|:", modulus) 
print("faseforskyvning [deg]:", argument)



#deloppgave d

# Beregn Bode-data
w, mag, phase = sig.bode(system)
# Finen absolutt magnitude
realmag = 10**(mag/20) 

# Definerer frekvensene vi vil sjekke
w_targets = [500, 1000, 2000, 4000]

# Beregner verdier spesifikt for disse frekvensene
w_vals, mag_vals, phase_vals = sig.bode(system, w=w_targets)

# lager tabell for svarverdier 
print(f"{'Frekvens [w]':<15} | {'Mag [dB]':<12} | {'Absolutt |H|':<15} | {'Fase [rad]':<12}")
print("-" * 65)


for i in range(len(w_targets)):
    abs_mag = 10**(mag_vals[i]/20)
    # Konverterer her:
    phase_rad = np.deg2rad(phase_vals[i]) 

    print(f"{w_targets[i]:<15} | {mag_vals[i]:<12.2f} | {abs_mag:<15.4f} | {phase_rad:<12.4f}")



# Plotting for bode plot
plt.figure()
plt.semilogx(w, mag)    # Bode Magnitude plot
plt.title('Forsterkning i dB')
plt.xlabel('vinkelfart')
plt.ylabel('amplitude')
plt.grid()

plt.figure()
plt.semilogx(w, mag)
plt.scatter(w_targets, mag_vals, color='red') # Markerer de 4 punktene
plt.title('Forsterkning i dB')
plt.grid()

plt.figure()
plt.semilogx(w, realmag) 
plt.title('Absolutt forsterkning')
plt.grid()

plt.figure()
plt.semilogx(w, phase)  # Bode Phase plot (tidsforskyvning)
plt.title('Faseforskyvning i $^\circ$')
plt.xlabel('$\omega\,$(rad/s)')
plt.ylabel('faseforskyvning')
plt.grid()
plt.show()


plt.plot(t, v_inn)
plt.plot(t, v_ut)
plt.xlabel('tid')
plt.ylabel('spenning')
plt.legend()
plt.grid()
plt.show()




