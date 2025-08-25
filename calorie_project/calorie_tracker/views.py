from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import FoodItem
from .forms import FoodItemForm

def dashboard(request):
    today = timezone.now().date()
    food_items = FoodItem.objects.filter(date_consumed=today)
    total_calories = sum(item.calories for item in food_items)
    
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calorie_tracker:dashboard')
    else:
        form = FoodItemForm()
    
    context = {
        'food_items': food_items,
        'total_calories': total_calories,
        'form': form,
        'today': today,
    }
    return render(request, 'calorie_tracker/dashboard.html', context)

def delete_food_item(request, pk):
    food_item = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        food_item.delete()
    return redirect('calorie_tracker:dashboard')

def reset_day(request):
    today = timezone.now().date()
    if request.method == 'POST':
        FoodItem.objects.filter(date_consumed=today).delete()
    return redirect('calorie_tracker:dashboard')