---
title: Automatic Generation of Test Reports
author: Kristoffer Nordström
---

# Introduction

The generation of a [traceability
matrix](https://en.wikipedia.org/wiki/Traceability_matrix) with, e.g., a
*requirements specification* and a *test report*, can be a tedious business.
Especially if this works has to be repeated a number of times because, e.e.,
the requirements have changed.

This does not lend to any agile developement where mistakes can be found early
and corrected as high up as possible in the chain. Change the requirements
instead of writing cumbersome tests because some hard-to-test item has been
requried.

The following sections will assume a unit-test output, i.e. a xUnit XML file,
as the source *test report*. It can extended to other data sources fairly
straigtforward. The requirements will have ID with the following format:
*SW-[0-9]+*, e.g., SW-100. If the dash ( - ) isn't allowed for syntactical
reasons, it's replaced by an underscore ( _ ).

# Naive solution

The simple solution would be to name your tests (or parts thereof) with the
requirement number that is being tested.  In the following example, the test
function `testExecuteOnDisabledControl_SW_100` would be used as a *test
criteria* to state whether requirement SW-100 has been implemented
successfully.

```java
class ClickActionTest {

    [...]
    @Test
    public void testExecuteOnDisabledControl_SW_100() {
```


## Problems

This has a few drawbacks that felt needing some attention. 

### Naming

It's obvious that if the requirements and tests aren't nearly a n-to-n
mapping, that the names will become a unreadable mess. Imagine
`testExecuteOnDisabledControl_SW_100__SW_101__SW120__SW_121` as absurdum.

This problem will not be addressed here, as it's considered a implementation
specific problem. For unit-tests it's probably already solved with, e.g.,
[*traits*](http://www.brendanconnolly.net/organizing-tests-with-xunit-
traits/).

### Requirement vs. Test Coherence

The can of worms of validation is not going to be opened here. It is assumed
the test engineer understands the requirements correctly and writes tests correctly.

The challenge at hand is to ensure that tests are updated if the requirements
change. Hence there is a need to transfer information about the requirement's
state to the unit-test.


# Hashed Requirements

Instead of just using the name of the requirement in the test, information
about the state of the requirement is used as well. To avoid external
dependencies, only information in the requirement's specification can be used.

It is proposed to use the following items. This can easily be extended however.

* Title,
* Description,
* Verification Method, e.g., analysis.

Using a hashing function, e.g., SHA-256, this information can be condensed
into a 64-bit string. Our previous example can now be uniquely identified 
by e.g., *SW-100-deadbeef*. The corresponding test would look as follows: 
`testExecuteOnDisabledControl_SW_100_deadbeef`.


# Backward Traceability 

The term *backward traceability* as defined [here](https://web.archive.org/web
/20100601214050/http://www.compaid.com/caiinternet/ezine/westfall-
bidirectional.pdf).  This corresponds to *horizontal traceability* in the V-process.


# Requirements Traceability 

* Forward traceability
* Follow the V
* Traceability information
* Basically the same methodology

