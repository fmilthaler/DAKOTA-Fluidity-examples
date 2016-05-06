L=1e6;
dx=8e3;
Point(1) = {0.0, 0.0, 0.0, dx};
Extrude {L, 0, 0} {
  Point{1};
}
Extrude {0, L, 0} {
  Line{1};
}
Line Loop(6) = {2, -4, -1, 3};
Plane Surface(7) = {6};
Physical Surface(1) = {5};
Physical Line(3) = {1}; // south
Physical Line(4) = {2}; // north
Physical Line(5) = {3}; // west
Physical Line(6) = {4}; // east
