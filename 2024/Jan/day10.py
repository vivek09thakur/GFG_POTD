class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		#Complete the function
        mod_dict = {0: -1}
        max_length = 0
        current_sum = 0
 
        for i in range(n):
            current_sum += arr[i]
 
            modulus = current_sum % K
 
            if modulus in mod_dict:
                max_length = max(max_length, i - mod_dict[modulus])
            else:
                mod_dict[modulus] = i
 
        return max_length
