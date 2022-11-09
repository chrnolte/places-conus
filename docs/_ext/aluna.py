from collections import defaultdict

from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, Index
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode


class AlunaDirective(ObjectDescription):
    """A custom directive that describes a aluna."""

    has_content = True
    required_arguments = 1
    option_spec = {
        'contains': directives.unchanged_required,
    }

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text=sig)
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        signode['ids'].append('aluna' + '-' + sig)
        if 'contains' in self.options:
            ingredients = [
                x.strip() for x in self.options.get('contains').split(',')]

            alunas = self.env.get_domain('aluna')
            alunas.add_aluna(sig, ingredients)


class IngredientIndex(Index):
    """A custom index that creates an ingredient matrix."""

    name = 'ingredient'
    localname = 'Ingredient Index'
    shortname = 'Ingredient'

    def generate(self, docnames=None):
        content = defaultdict(list)

        alunas = {name: (dispname, typ, docname, anchor)
                   for name, dispname, typ, docname, anchor, _
                   in self.domain.get_objects()}
        aluna_ingredients = self.domain.data['aluna_ingredients']
        ingredient_alunas = defaultdict(list)

        # flip from aluna_ingredients to ingredient_alunas
        for aluna_name, ingredients in aluna_ingredients.items():
            for ingredient in ingredients:
                ingredient_alunas[ingredient].append(aluna_name)

        # convert the mapping of ingredient to alunas to produce the expected
        # output, shown below, using the ingredient name as a key to group
        #
        # name, subtype, docname, anchor, extra, qualifier, description
        for ingredient, aluna_names in ingredient_alunas.items():
            for aluna_name in aluna_names:
                dispname, typ, docname, anchor = alunas[aluna_name]
                content[ingredient].append(
                    (dispname, 0, docname, anchor, docname, '', typ))

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())

        return content, True


class AlunaIndex(Index):
    """A custom index that creates an aluna matrix."""

    name = 'aluna'
    localname = 'Aluna Index'
    shortname = 'Aluna'

    def generate(self, docnames=None):
        content = defaultdict(list)

        # sort the list of alunas in alphabetical order
        alunas = self.domain.get_objects()
        alunas = sorted(alunas, key=lambda aluna: aluna[0])

        # generate the expected output, shown below, from the above using the
        # first letter of the aluna as a key to group thing
        #
        # name, subtype, docname, anchor, extra, qualifier, description
        for _name, dispname, typ, docname, anchor, _priority in alunas:
            content[dispname[0].lower()].append(
                (dispname, 0, docname, anchor, docname, '', typ))

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())

        return content, True


class AlunaDomain(Domain):

    name = 'aluna'
    label = 'Aluna Sample'
    roles = {
        'ref': XRefRole()
    }
    directives = {
        'aluna': AlunaDirective,
    }
    indices = {
        AlunaIndex,
        IngredientIndex
    }
    initial_data = {
        'alunas': [],  # object list
        'aluna_ingredients': {},  # name -> object
    }

    def get_full_qualified_name(self, node):
        return '{}.{}'.format('aluna', node.arguments[0])

    def get_objects(self):
        yield from self.data['alunas']

    def resolve_xref(self, env, fromdocname, builder, typ, target, node,
                     contnode):
        match = [(docname, anchor)
                 for name, sig, typ, docname, anchor, prio
                 in self.get_objects() if sig == target]

        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]

            return make_refnode(builder, fromdocname, todocname, targ,
                                contnode, targ)
        else:
            # print('Awww, found nothing')
            return None

    def add_aluna(self, signature, ingredients):
        """Add a new aluna to the domain."""
        name = f'aluna.{signature}'
        anchor = f'aluna-{signature}'

        self.data['aluna_ingredients'][name] = ingredients
        # name, dispname, type, docname, anchor, priority
        self.data['alunas'].append(
            (name, signature, 'Aluna', self.env.docname, anchor, 0))


def setup(app):
    app.add_domain(AlunaDomain)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

