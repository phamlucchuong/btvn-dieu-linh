public class overloading {

    public static int plus(int a, int b) {
        return a + b;
    }
    public static float plus(float a, float b) {
        return a + b;
    }
    public static double plus(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        System.out.println(plus(2, 3));
        System.out.println(plus(2.f, 3.f));
        System.out.println(plus(2.d, 3.d));
    }
}