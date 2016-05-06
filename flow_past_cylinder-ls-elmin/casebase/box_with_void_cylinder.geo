//

lf = {elmin};
lm = 2*lf;
lc = 5*lf;
mc = 0.01;

// inner circle:
Point(1) = {0.2,0.2,0,mc};
Point(2) = {0.25,0.2,0,lf};
Point(3) = {0.2,0.25,0,lf};
Point(4) = {0.15,0.2,0,lf};
Point(5) = {0.2,0.15,0,lf};
Circle(1) = {2,1,3};
Line(101) = {1,2};
Circle(2) = {3,1,4};
Line(102) = {1,3};
Circle(3) = {4,1,5};
Line(103) = {1,4};
Circle(4) = {5,1,2};
Line(104) = {1,5};
Line Loop(1) = {101, 1, -102};
Line Loop(2) = {102, 2, -103};
Line Loop(3) = {103, 3, -104};
Line Loop(4) = {104, 4, -101};
Ruled Surface(1) = {1};
Ruled Surface(2) = {2};
Ruled Surface(3) = {3};
Ruled Surface(4) = {4};
Line Loop(108) = {4, 1, 2, 3};



// box points:
Point (6) = {0, 0, 0, lm};
Point (7) = {2.2, 0, 0, lc};
Point (8) = {2.2, 0.41, 0, lc};
Point (9) = {0, 0.41, 0, lm};
Line (5) = {9, 6};
Line (6) = {9, 8};
Line (7) = {6, 7};
Line (8) = {8, 7};
Line Loop (10) = {6, 8, -7, -5};
// Box surface:
Plane Surface(109) = {10, 108};



// Physical IDs:
//front/inlet:
Physical Line(1) = {5};
//top and bottom
Physical Line(2) = {6, 7};
//back/outlet:
Physical Line(3) = {8};
// Cylinder:
Physical Line(4) = {1, 2, 3, 4};
// Surface
Physical Surface(1) = {109};


// For the void case:
Delete{
  Surface{1,2,3,4};
}



