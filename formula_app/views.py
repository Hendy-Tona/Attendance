from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import FormulaForm

def input_formula(request):
    if request.method == 'POST':
        form = FormulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = FormulaForm()
    return render(request, 'formula_app/input_formula.html', {'form': form})