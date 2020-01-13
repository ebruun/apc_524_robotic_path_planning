Examples
============

Showing the input/output from several program runs.

Two domains defined with the following types of geometry::

	Rectangle
	Circle

There following three shapes are used to define both obstacles and goals::

	Rectangle
	Circle
	Freeform

The domains are solved with the following algorithms::

	Basic RRT
	RRT Star

Circular Domain
****************

Input Files
-----------

.. literalinclude:: ../../../src_pathplanner/input/user_input_files/circle_regular_obstacles.json
   :language: json
   :linenos:
   :emphasize-lines: 24
   :caption: Basic RRT

Basic RRT Output
----------------
Show plots and results

.. raw:: html
	:file: ../../../src_pathplanner/output/output_files/circle_regular_obstacles.html

RRT Star Output
----------------
Show plots and results


Rectangular Domain
******************

Input Files
-----------

Basic RRT Output
----------------
Show plots and results

RRT Star Output
----------------
Show plots and results