from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Component
from .forms import ComponentForm

@login_required
def create_component(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)

        if form.is_valid():
            component = form.save(commit=False)
            component.user = request.user
            component.save()

            return redirect('components:list_components')

    else:
        form = ComponentForm()

    return render(request, 'create_components.html', {'form': form})

@login_required
def list_components(request):
    components = Component.objects.filter(user=request.user).order_by("id")
    paginator = Paginator(components, 5)

    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_components.html', {'page_obj': page_obj})

@login_required
def edit_component(request, component_id):
    component = get_object_or_404(Component, id=component_id, user=request.user)

    if request.method == 'POST':
        form = ComponentForm(request.POST, instance=component)

        if form.is_valid():
            form.save()
            return redirect('components:list_components')

    else:
        form = ComponentForm(instance=component)

    return render(request, 'edit_components.html', {'form': form})

@login_required
@require_POST
def delete_component(request, component_id):
    component = get_object_or_404(Component, id=component_id, user=request.user)

    component.delete()
    messages.success(request, "Componente excluído com sucesso.")

    return redirect('components:list_components')