def even_odd_filter(**kwargs):
    if 'odd' in kwargs:
        kwargs['odd'] = [int(i) for i in kwargs['odd'] if i % 2 != 0]

    if 'even' in kwargs:
        kwargs['even'] = [int(j) for j in kwargs['even'] if j % 2 == 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
