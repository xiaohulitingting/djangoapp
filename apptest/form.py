from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                               error_messages={'required': "用户名不能为空"})
    password = forms.CharField(max_length=120,
                               min_length=6,
                               required=True,
                               error_messages={'required': "密码不能为空"})
    def clean(self):
        # 用户名
        try:
            username = self.cleaned_data['username']
        except Exception as e:
            raise forms.ValidationError(u"用户名不能为空")
        '''
                # 验证邮箱
                 user = User.objects.filter(username=email)
        if user:  # 邮箱已经被注册了
            raise forms.ValidationError(u"邮箱已被注册")

       '''
        try:
            password = self.cleaned_data['password']
        except Exception as e:
            raise forms.ValidationError(u"请输入至少6位密码")

        return self.cleaned_data