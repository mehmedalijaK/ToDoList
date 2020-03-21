from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=70,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Do homework',
                                      'aria-label': 'Todo', 'aria-describedby': 'add-btn'}))
