public class Lasagna {

    private int remainingMinutes;

    public Lasagna() {
        remainingMinutes = 40;
    }

    public int expectedMinutesInOven() {
        return remainingMinutes;
    }

    public int remainingMinutesInOven(int minutesInOven) {
        return remainingMinutes - minutesInOven;
    }

    public int preparationTimeInMinutes(int layers) {
        return layers * 2;
    }

    public int totalTimeInMinutes(int layers, int minutesInOven) {
        return (layers * 2) + minutesInOven;
    }
}
