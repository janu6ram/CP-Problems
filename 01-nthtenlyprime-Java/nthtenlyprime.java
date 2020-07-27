// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n
// # and returns the nth Additive Prime, which is a prime number such that
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


class nthtenlyprime {
	public int fun_nthtenlyprime(int n){
		int[] tenly_primes = new int[n+1];
		int i = 2;
		int pos = 0;
		while (tenly_primes.length != n+1) {
			if (isPrime(i) && sumPrime(i)){
				tenly_primes[pos] = i;
				pos++;
			}
			i++;
		}
		return tenly_primes[n];


	}
	public boolean isPrime(int n) {
		if (n <= 1){
			return false;
		}
		if (n <= 3){
			return true;
		}
		if (n%2 == 0 || n%3 == 0){
			return false;
		}
		int i = 5;
		while (i*i <= n){
			if (n%i == 0 || n%(i+2) == 0){
				return false;
			}
			i += 6;
		}
		return true;
	}
	public boolean sumPrime(int num){
		int sum = 0;
		while(num != 0){
			int rem = num%10;
			num = num/10;
			sum += rem;
		}
		return isPrime(sum);
	}

}