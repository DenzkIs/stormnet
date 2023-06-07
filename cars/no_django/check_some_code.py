# a = 'zhurid.dk@tut.by'
# b = 'zhurid.by@re.r1'
# c = 'zhurid dk@tut.by'
# d = 'zhurid@.by'
# e = 'zhu.rid@dvdsdv'
# f = 'zhu@rid@dvds.dv'
# g = 'zhurid@dvds.d1'
# h = 'zhu*rid@dvds.d1'
#
#
# def validate_email(email: str):
#     characters = 'abcdefghijklmnopqrstuvwxyz.@_-'
#     email = email.lower()
#     if email.count('@') != 1 or len(email) > 50:
#         return False
#     name, domen = email.split('@')
#     print(name, '---', domen)
#     if domen.count('.') != 1:
#         return False
#     for i in name:
#         if i not in characters:
#             return False
#     dom, country = domen.split('.')
#     print(dom, '----', country)
#     if not dom.isalpha() or not country.isalpha() or len(dom) < 2 or len(country) < 2:
#         return False
#     return True
#
#
# print(validate_email(b))


