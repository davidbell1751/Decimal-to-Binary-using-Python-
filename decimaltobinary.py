
# david bell
# cs 499 SNHU
# Algortithm for Finding Binary from a Decimal



# Reverse Engineer Decimal to Binary from Java to Python

# Java Algorithm

"""
import java.util.Scanner                // import scanner class

    public class DecimalToBinary {          

        public static void main(String[] args) {

            int number, i=0;                                    // declare int number
            int binary[]=new int[100];                          // binary int variable  = new int with size of 100
            Scanner user_input=new Scanner(System.in);          // scanner object
            System.out.print("Enter decimal number :");         // user input
            number=user_input.nextInt();                        // number is equal to user input


             while(number!=0)                           // number has to be any number not zero
             {
                 binary[i] = number%2;      // calculate remainder and store in i    the result will be zero or 1 
                 number = number/2;         // that number will then be divided by 2
                 i++;
             }

             System.out.print("Binary value is" ");
             for(int j=i-1;j>=0,j--)            //  for loop  // j = i - 1   // j greater then or equal to zero  // j is incremented by 1

             {
                 System.out.print(""+binary[j]);
             }
        }
    }

"""



def decimal_to_binary(deci, number_bits=8):          # funciton decimal to binary    number of bits = 8
    binary_list = []                               # accumulate a list with this variable
    j = deci                                    # initial decimal number and save it into x

    for _ in range(number_bits):                         # using for loop in the range of 8 bits
        bitList = j % 2                                 # find the remainder and then store for later  / modulas of the original bit   even number right most value is zero
        binary_list.append(bitList)                        # append this bit to the list
        j //= 2                                     # get current value, divided by 2  / floor division  --> //
    return binary_list[::-1]                           

print(decimal_to_binary(8, number_bits=8))              # print decimal to binary using 8 bits