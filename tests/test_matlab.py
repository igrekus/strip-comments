import strip_comments.strip as strip

source = '''MATLAB
In MATLAB's programming language, the '%' character indicates a single-line comment. Multi line comments are also available via `%{` and `%}` brackets and can be nested, e.g.

% These are the derivatives for each term
d = [0 -1 0];

%{
  %{
    (Example of a nested comment, indentation is for cosmetics (and ignored).)
  %}
  We form the sequence, following the Taylor formula.
  Note that we're operating on a vector.
%}
seq = d .* (x - c).^n ./(factorial(n))

% We add-up to get the Taylor approximation
approx = sum(seq)
'''

expected = '''MATLAB
In MATLAB's programming language, the '%' character indicates a single-line comment. Multi line comments are also available via `%{` and `%}` brackets and can be nested, e.g.


d = [0 -1 0];


seq = d .* (x - c).^n ./(factorial(n))


approx = sum(seq)
'''


def test_strips_matlab():

    assert strip.strip(source, language='matlab') == expected
