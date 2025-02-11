from .component import Component


class Section(Component):
    @property
    def type_of(self) -> str:
        return 'section'
