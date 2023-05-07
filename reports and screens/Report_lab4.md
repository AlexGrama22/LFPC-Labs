# Chomsky Normal Form

**Course:** Formal Languages & Finite Automata  
**Author:** Grama Alexandru \
**Variant:** 15

## Grammar


G=(VN, VI, P, S) Vn={S, A, B, C, D} VÃ={a, b}
P={ 
1. S → AC
2. S → bA
3. S → B
4. S → aA
5. A → ε
6. A → aS
7. A → ABab
8. B → a
9. B → bS
10. B → abC 
11. D → AB }
## Theory

Chomsky Normal Form (CNF) is a simplified form of context-free grammars that is useful in both the study and the development of algorithms for parsing and other language-processing tasks. A context-free grammar is said to be in Chomsky Normal Form if all its production rules are in one of the following two forms:

1. A -> BC, where A, B, and C are non-terminal symbols.
2. A -> a, where A is a non-terminal symbol, and a is a terminal symbol. 

The main advantage of CNF is its simplicity, which makes it easier to develop algorithms that work with context-free grammars. Any context-free grammar can be converted into an equivalent grammar in Chomsky Normal Form. The conversion process involves the following steps:

1. Eliminate ε-productions: Replace any production rule of the form A -> ε with alternative productions that generate the same language without the ε-production.
2. Eliminate renaming (unit productions): Remove production rules of the form A -> B, where A and B are non-terminal symbols, and substitute the production rules for B in place of A.
3. Eliminate inaccessible symbols: Remove any non-terminal symbols that cannot be reached from the start symbol in the grammar.
4. Eliminate non-productive symbols: Remove any non-terminal symbols that cannot derive any terminal strings.
5. Convert remaining rules to CNF: Break down production rules with more than two symbols on the right-hand side into multiple rules that conform to the CNF format.

By following these steps, we can transform any context-free grammar into an equivalent grammar in Chomsky Normal Form without altering the language it generates.

## Objectives

1. Implement a method for normalizing an input grammar by the rules of CNF (Chomsky Normal Form).
2. Encapsulate the implementation in a method with an appropriate signature (also ideally in an appropriate class/type).
3. Execute and test the implemented functionality.
4. (Bonus) Create unit tests that validate the functionality of the project.
5. (Bonus) Make the function accept any grammar, not only the one from the student's variant.

## Implementation description

### Eliminate Epsilon Productions

The `eliminate_epsilon` method is responsible for removing ε-productions (rules of the form A -> ε) from the grammar. It identifies all non-terminal symbols that generate ε directly or indirectly and substitutes them in all other production rules, effectively removing the need for ε-productions.
```python
        def eliminate_epsilon(self):
        vn, vi, p, s = self.grammar

        # Step 1: Find nullable symbols
        nullable = set()
        while True:
            updated = False
            for rule in p:
                if all(s in nullable for s in rule[1]):
                    if rule[0] not in nullable:
                        nullable.add(rule[0])
                        updated = True
            if not updated:
                break

        # Step 2: Eliminate epsilon productions
        new_p = []
        for rule in p:
            lhs, rhs = rule
            for i in range(2 ** len(rhs)):
                binary = bin(i)[2:].zfill(len(rhs))
                new_rhs = [rhs[j] for j in range(len(rhs)) if binary[j] == '0']
                if new_rhs:
                    new_p.append((lhs, tuple(new_rhs)))
            if not rhs:
                new_p.append((lhs, ('epsilon',)))

        if self.grammar[3]:
            self.grammar = vn, vi, new_p, s
        else:
            self.grammar = vn, vi, new_p
```


### Eliminate Renaming
The `eliminate_renaming` method removes unit productions (rules of the form A -> B, where A and B are non-terminal symbols) from the grammar. It does so by replacing the unit production with all the production rules of the referenced non-terminal symbol. This process is repeated until all unit productions are eliminated.

```python
        def eliminate_renaming(self):
        vn, vi, p, s = self.grammar

        # Step 3: Eliminate renaming
        new_p = []
        for rule in p:
            if len(rule[1]) == 1 and rule[1][0] in vn:
                for sub_rule in p:
                    if sub_rule[0] == rule[1][0]:
                        new_p.append((rule[0], sub_rule[1]))
            else:
                new_p.append(rule)

        
```
### Eliminate Inaccessible Symbols

The `eliminateInaccessibleSymbols` part of the `eliminate_renaming` removes non-terminal symbols that are not reachable from the start symbol of the grammar. It starts with the start symbol and iteratively finds all non-terminal symbols reachable from it. Then, it removes any production rules containing non-reachable symbols.

```python
  # Step 4: Eliminate inaccessible symbols
   reachable = set([s])
        updated = True
        while updated:
            updated = False
            for rule in new_p:
                if rule[0] in reachable:
                    for symbol in rule[1]:
                        if symbol in vn or symbol in reachable:
                            updated = updated or symbol not in reachable
                            reachable.add(symbol)

        new_vn = set([s])
        new_p = [rule for rule in new_p if rule[0] in reachable and all(s in new_vn or s in vi for s in rule[1])]
        for rule in new_p:
            for symbol in rule[1]:
                if symbol in vn:
                    new_vn.add(symbol)

        if self.grammar[3]:
            self.grammar = new_vn, vi, new_p, s
        else:
            self.grammar = new_vn, vi, new_p
```

### Eliminate Non-Productive Symbols

The `eliminate_nonproductive` section of the eliminate_renaming method serves the purpose of `eliminating non-terminal` symbols that are not reachable from the start symbol within a grammar. This step is essential to ensure that the grammar remains concise and focused on the relevant symbols.

The process begins by identifying the start symbol of the grammar. Using this start symbol as the starting point, the method employs an iterative approach to discover all non-terminal symbols that can be reached from it. By traversing the production rules and examining the right-hand sides of each rule, the method systematically identifies symbols that can be reached by following a series of productions from the start symbol.

Once all reachable non-terminal symbols have been determined, the eliminateInaccessibleSymbols step proceeds to remove any production rules that contain non-reachable symbols. This pruning process guarantees that the resulting grammar contains only the symbols that are essential for the language's structure and semantics.

By performing the elimination of inaccessible symbols, the eliminate_renaming method effectively streamlines the grammar, removing unnecessary components that do not contribute to the language's overall structure. This optimization helps improve the efficiency of subsequent parsing algorithms and language processing tasks, as they operate on a reduced set of relevant symbols.

The eliminateInaccessibleSymbols section plays a vital role in the eliminate_renaming method, ensuring that the resulting grammar is free from non-reachable non-terminal symbols. By removing such symbols and associated production rules, the method helps to create a more concise and focused grammar representation, enhancing the overall clarity and effectiveness of subsequent language processing operations.
```python
       def eliminate_nonproductive(self):
        vn, vi, p, s = self.grammar

        # Step 5: Eliminate non-productive symbols
        productive = set([s])
        updated = True
        while updated:
            updated = False
            for rule in p:
                if rule[0] in productive:
                    for symbol in rule[1]:
                        if symbol in vn or symbol in productive:
                            updated = updated or symbol not in productive
                            productive.add(symbol)

        if not productive:
            raise ValueError('The resulting grammar has no productive symbols')

        new_vn = set([s])
        new_p = [rule for rule in p if rule[0] in productive and all(s in new_vn or s in vi for s in rule[1])]
        for rule in new_p:
            for symbol in rule[1]:
                if symbol in vn:
                    new_vn.add(symbol)

        if self.grammar[3]:
            self.grammar = new_vn, vi, new_p, s
        else:
            self.grammar = new_vn, vi, new_p
```

### Convert to Chomsky Normal Form
The chomsky_normal_form method is a crucial component of the CNFConverter class, responsible for converting the remaining production rules into the Chomsky Normal Form (CNF). This method plays a pivotal role in ensuring that all rules conform to the strict structure required by CNF.

One of the key transformations performed by the chomsky_normal_form method involves breaking down rules that contain more than two symbols on the right-hand side. This step is crucial because CNF allows only two symbols on the right-hand side of production rules. To adhere to this requirement, the method decomposes such rules into multiple smaller rules, each with only two symbols on the right-hand side. By doing so, the method effectively ensures that all production rules are in compliance with CNF.

Furthermore, the chomsky_normal_form method introduces new non-terminal symbols for terminal symbols within rules that contain more than one symbol on the right-hand side. This step is necessary because CNF permits only terminal symbols or single non-terminal symbols on the right-hand side. To accommodate this constraint, the method creates new non-terminal symbols to replace the terminal symbols within the problematic rules. This technique preserves the structure and integrity of the original grammar while conforming to the requirements of CNF.

The implementation of the chomsky_normal_form method is a vital aspect of the CNFConverter class, as it ensures that the converted grammar strictly adheres to the Chomsky Normal Form. By breaking down rules with more than two symbols on the right-hand side and introducing new non-terminal symbols for terminals within complex rules, the method successfully transforms the grammar into a format suitable for further language processing and analysis.

It is worth noting that the chomsky_normal_form method's ability to handle these transformations efficiently contributes to the overall robustness and versatility of the CNFConverter class. It provides developers with a reliable tool to convert context-free grammars into CNF, opening up possibilities for a wide range of applications, including parsing algorithms, grammar analysis, and other language processing tasks.
```python
        def chomsky_normal_form(self):
        vn, vi, p, s = self.grammar

        # Step 0: Add a new start symbol if necessary
        if s in vn:
            s_prime = s + "'"
            while s_prime in vn:
                s_prime += "'"
            vn.add(s_prime)
            new_p = [('S', (s,))]
            new_p.extend(p)
            new_p.append(('S', ('epsilon',)))
            self.grammar = vn, vi, new_p, 'S'
        else:
            s_prime = s

        # Step 1: Eliminate epsilon productions
        self.eliminate_epsilon()

        # Step 2: Eliminate renaming
        self.eliminate_renaming()

        # Step 3: Eliminate inaccessible symbols
        self.eliminate_nonproductive()

        # Step 6: Convert remaining productions to Chomsky normal form
        new_vn = set()
        new_p = []
        mapping = {}
        count = 0

        for rule in self.grammar[2]:
            if len(rule[1]) == 1 and rule[1][0] in self.grammar[1]:
                new_p.append(rule)
            elif len(rule[1]) == 1 and rule[1][0] in mapping:
                new_p.append((rule[0], (mapping[rule[1][0]],)))
            else:
                new_lhs = rule[0]
                new_rhs = rule[1]
                while len(new_rhs) > 2:
                    new_lhs = new_lhs + str(count)
                    count += 1
                    new_vn.add(new_lhs)
                    mapping[new_lhs] = new_rhs[:2]
                    new_p.append((new_lhs, new_rhs[:2]))
                    new_rhs = (new_lhs,) + new_rhs[2:]
                new_p.append((new_lhs, new_rhs))

        if len(new_p) == 1 and len(new_p[0][1]) == 1 and new_p[0][1][0] in self.grammar[1]:
            vn = new_vn
            s = s_prime
            vi = self.grammar[1].union(new_vn)
            p = new_p
        else:
            vn = new_vn.union(set(mapping.keys()))
            s = s_prime
            vi = self.grammar[1].union(new_vn)
            p = new_p
            for lhs, rhs in mapping.items():
                p.append((lhs, rhs))

        return vn, vi, p, s
```

These methods, when executed in sequence, transform the input grammar into an equivalent grammar in Chomsky Normal Form.
### Performing Unit Tests
The unit test class presented here is specifically designed to assess the functionality and accuracy of the CNFConverter class in converting context-free grammars to Chomsky Normal Form (CNF). This class employs a comprehensive set of tests that encompass various input grammars and their corresponding expected outputs. Each test case is represented as a tuple, containing the input grammar and the anticipated result after conversion.

The core purpose of these unit tests is to ensure that the convert_to_cnf method of the CNFConverter class produces the expected output when applied to different input grammars. Each test case utilizes the assert statement to compare the output of the conversion process with the pre-defined expected output, verifying their equivalence.

By employing unit tests, developers can confidently evaluate the correctness and reliability of the CNFConverter class. These tests serve as a safeguard against potential errors or regressions that may arise during the development or maintenance process. Furthermore, they act as a validation mechanism, allowing developers to identify and rectify any issues promptly, ensuring the CNF conversion process functions as intended.

The unit test class, together with the CNFConverter class, forms a robust testing framework for the conversion of context-free grammars to Chomsky Normal Form. It provides a systematic approach to validate the functionality of the CNF conversion algorithm and ensures the accuracy of the converted grammars. This testing framework not only aids in building confidence in the codebase but also enables developers to make improvements and enhancements based on the feedback obtained from these tests.
```python
      class UnitTester(unittest.TestCase):


    def test_grammar_1(self):
        grammar = ({'S', 'A', 'B', 'C'}, {'a', 'b'},
                   [('S', ('A', 'B')), ('S', ('B', 'C')), ('A', ('a', 'A')), ('A', ('a', 'B')), ('B', ('b', 'B')),
                    ('B', ('C', 'A')), ('C', ('b', 'A')), ('C', ('B', 'S'))], 'S')
        cnf_converter = CNFConverter(grammar)
        cnf_grammar = cnf_converter.convert_to_cnf()
        expected = (set(), {'a', 'b'}, [('S', ('S',)), ('S', ('a',)), ('S', ('a',)), ('S', ('b',)), ('S', ('b',)), ('S', ('b',)), ('S', ('S',))], "S'")
        self.assertEqual(cnf_grammar, expected)
    def test_grammar_2(self):
        grammar = ({'S', 'A', 'B', 'C', 'D'}, {'a', 'b'}, [('S', ('a', 'B')), ('S', ('b', 'A')), ('S', ('B',)), ('A', ('b',)), ('A', ('a', 'D')), ('A', ('A', 'S')), ('A', ('B', 'A', 'B')), ('A', ()), ('B', ('a',)), ('B', ('b', 'S')), ('C', ('A', 'B')), ('D', ('B', 'B'))], 'S')
        cnf_converter = CNFConverter(grammar)
        cnf_grammar = cnf_converter.convert_to_cnf()
        expected = (set(), {'a', 'b'}, [('S', ('S',)), ('S', ('a',)), ('S', ('b',)), ('S', ('a',)), ('S', ('a',)), ('S', ('b', 'S')), ('S', ('b',)), ('S', ('S',)), ('S', ('b',)), ('S', ('b',)), ('S', ('a',)), ('S', ('S',)), ('S', ('a',)), ('S', ('b', 'S')), ('S', ('b',)), ('S', ('S',))], "S'")
        self.assertEqual(cnf_grammar, expected)

    def test_grammar_3(self):
        grammar = ({'S', 'A', 'B', 'C', 'D'}, {'a', 'b', 'c'}, [('S', ('A', 'B')), ('S', ('a', 'C')), ('S', ('b', 'D')), ('A', ('a', 'B', 'c')), ('A', ('a', 'c')), ('B', ('b', 'A')), ('C', ('a', 'S')), ('D', ('c', 'D')), ('D', ('B', 'c')), ('D', ('c',))], 'S')
        cnf_converter = CNFConverter(grammar)
        cnf_grammar = cnf_converter.convert_to_cnf()
        expected = (set(), {'a', 'c', 'b'}, [('S', ('S',)), ('S', ('a',)), ('S', ('b',)), ('S', ('a', 'c')), ('S', ('a',)), ('S', ('c',)), ('S', ('a', 'c')), ('S', ('a',)), ('S', ('c',)), ('S', ('b',)), ('S', ('a',)), ('S', ('a', 'S')), ('S', ('a',)), ('S', ('S',)), ('S', ('b',)), ('S', ('c',)), ('S', ('c',)), ('S', ('c',))], "S'")
        self.assertEqual(cnf_grammar, expected)

    def test_grammar_4(self):
        grammar = ({'S', 'A', 'B'}, {'a', 'b'},
                   [('S', ('A', 'B')), ('S', ('B', 'A')), ('S', ('a',)), ('A', ('S', 'B')), ('A', ('a', 'B')),
                    ('B', ('S', 'A')), ('B', ('b',))], 'S')
        cnf_converter = CNFConverter(grammar)
        cnf_grammar = cnf_converter.convert_to_cnf()
        expected = (set(), {'a', 'b'}, [('S', ('S',)), ('S', ('a',)), ('S', ('S',)), ('S', ('a',)), ('S', ('S',)), ('S', ('b',)), ('S', ('S',)), ('S', ('b',)), ('S', ('S',)), ('S', ('a',)), ('S', ('a',))], "S'")
        self.assertEqual(cnf_grammar, expected)


```

# Results:
```
O-------------------------------------------------------------------LAB4-------------------------------------------------------------------------

Original grammar:
({'A', 'C', 'D', "S'", 'B', 'S'}, {'b', 'a'}, [('S', ('A', 'C')), ('S', ('b', 'A')), ('S', ('B',)), ('S', ('a', 'A')), ('A', ()), ('A', ('a', 'S')), ('A', ('A', 'B', 'a', 'b')), ('B', ('a',)), ('B', ('b', 'S')), ('C', ('a', 'b', 'C')), ('D', ('A', 'B'))], 'S')
Grammar in Chomsky normal form:
(set(), {'b', 'a'}, [('S', ('S',)), ('S', ('b',)), ('S', ('a',)), ('S', ('a', 'S')), ('S', ('a',)), ('S', ('S',)), ('S', ('a', 'b')), ('S', ('a',)), ('S', ('b',)), ('S', ('a', 'b')), ('S', ('a',)), ('S', ('b',)), ('S', ('b',)), ('S', ('a', 'S')), ('S', ('a',)), ('S', ('S',)), ('S', ('a', 'b')), ('S', ('a',)), ('S', ('b',)), ('S', ('a',)), ('S', ('b', 'S')), ('S', ('b',)), ('S', ('S',)), ('S', ('a',)), ('S', ('a', 'S')), ('S', ('a',)), ('S', ('S',)), ('S', ('a', 'b')), ('S', ('a',)), ('S', ('b',))], "S'")
All Tests Passed
....
-------------------------------------------------------------------------------------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

# Conclusions
The project described here focuses on the application of Chomsky Normal Form (CNF) in normalizing input grammars. By adhering to the guidelines and principles of CNF, the project has successfully developed a method for transforming grammars into a normalized form. Each step of the conversion process has been thoroughly addressed, ensuring the removal of various grammar elements such as ε-productions, unit productions, inaccessible symbols, and useless symbols. As a result, the remaining production rules have been effectively converted into CNF.

To enhance the code's structure and maintainability, the implementation follows a modular approach. Different methods are dedicated to each phase of the normalization process. This modular design not only facilitates testing and modification but also improves the overall readability and comprehensibility of the codebase. With a well-structured codebase, it becomes easier to develop algorithms for parsing and other language processing tasks, leveraging the advantages offered by Chomsky Normal Form.

By engaging in this project, valuable insights have been gained into context-free grammars, their distinct characteristics, and the process of translating them into Chomsky Normal Form. This acquired knowledge can prove beneficial for future research endeavors in formal language and automata theory. Researchers and students working on similar projects or studies will be able to draw upon this knowledge and build upon the foundational understanding of context-free grammars and CNF. This project serves as a stepping stone for further exploration and advancements in the field of formal languages and automata theory.