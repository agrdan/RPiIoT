

class ComponentUtil:

    @staticmethod
    def placeComponent(component, row, column, sticky=None):
        if sticky is None:
            component.grid(row=row, column=column, padx=5, pady=5)
        else:
            component.grid(row=row, column=column, padx=5, pady=5, sticky=sticky)