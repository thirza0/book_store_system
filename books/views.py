from django.shortcuts import render , get_object_or_404

from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books': books})

def show(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/show.html', {'book':book})

def add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('books:index')
    
    return render(request, 'book/add.html', {'form': form})

def edit (request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, '更新成功')
        return redirect('books:index')

def delete(request):
    book = get_object_or_404(Book, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        book.delete()
        messages.success(request, '刪除成功')
        return redirect('books:index')

    return render(request, 'books/delete.html', {'form': form})
