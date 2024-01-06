int *p = new int(25);
float *q = new float(75.25);

// Custom data type
struct cust
{
   int p;
   cust(int q) : p(q) {}
};

// Works fine, doesn’t require constructor
cust* var1 = new cust; 