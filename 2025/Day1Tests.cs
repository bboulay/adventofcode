using Xunit;

public class Day1Tests
{
    [Fact]
    public void ExampleExercise1_ShouldReturn3()
    {
        int result = Day1.ExampleExercise1();
        Assert.Equal(3, result);
    }

    [Fact]
    public void Exercise1_ShouldReturn1123()
    {
        int result = Day1.Exercise1();
        Assert.Equal(1123, result);
    }

    [Fact]
    public void ExampleExercise2_ShouldReturn6()
    {
        int result = Day1.ExampleExercise2();
        Assert.Equal(6, result);
    }

    [Fact]
    public void Exercise2_ShouldReturn6695()
    {
        int result = Day1.Exercise2();
        Assert.Equal(6695, result);
    }
}
