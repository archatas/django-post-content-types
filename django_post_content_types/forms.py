from django import forms


class MultipartForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        min_length=3,
        error_messages={
            'required': 'Username is required',
            'min_length': 'Username must be at least 3 characters long',
            'max_length': 'Username cannot exceed 150 characters'
        }
    )
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'Email is required',
            'invalid': 'Please enter a valid email address'
        }
    )
    avatar = forms.FileField(
        required=False,
        error_messages={
            'invalid': 'Please upload a valid file'
        }
    )

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            if avatar.size > 5 * 1024 * 1024:
                raise forms.ValidationError('File size cannot exceed 5MB')
            
            allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
            if avatar.content_type not in allowed_types:
                raise forms.ValidationError(
                    f'Invalid file type. Allowed types: {", ".join(allowed_types)}'
                )
        return avatar

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            if not username.replace('_', '').isalnum():
                raise forms.ValidationError(
                    'Username can only contain letters, numbers, and underscores'
                )
        return username

