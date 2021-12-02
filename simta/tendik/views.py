from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from . import models
from .forms import MahasiswaForm

def dashboardView(request):
    return render(request, 'tendik/index.html')

def pembimbingView(request):
    return render(request, 'tendik/pembimbing.html')

# ----------------------Untuk Halaman Mahasiswa---------------------------------

# Tampilkan Data
def mahasiswaView(request):
    if request.POST:
        nama = request.POST['nama']
        nim = request.POST['nim']
        prodi = request.POST['prodi']
        fakultas = request.POST['fakultas']
        kelas = request.POST['kelas']
        semester = request.POST['semester']
        models.MahasiswaModel.objects.create(nama=nama, nim=nim, prodi=prodi, fakultas=fakultas, kelas=kelas, semester=semester)
        print(nim)
        
    mhs_table = models.MahasiswaModel.objects.all()
    return render(request, 'tendik/mahasiswa.html', {
        'tabel_mhs': mhs_table
    })

    # Hapus Data
def mahasiswaHapus(request, id):
    models.MahasiswaModel.objects.filter(pk=id).delete()
    return redirect('/tendik/mahasiswa')

# ------------------------------------------------------------

def pengajuanJudulView(request):
    return render(request, 'tendik/pengajuanjudul.html')

def proposalView(request):
    return render(request, 'tendik/proposal.html')

def tugasAkhirView(request):
    return render(request, 'tendik/tugas-akhir.html')