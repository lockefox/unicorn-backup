"""
Test Runner

..moduleauthor:: John Purcell <jpurcell.ee@gmail.com>
"""

import nox
import nox_poetry


@nox_poetry.session()
def test(session):
    session.run("poetry", "install", external=True)
    session.run("pytest")
