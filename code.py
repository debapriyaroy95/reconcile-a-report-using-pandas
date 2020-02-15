# --------------

import pandas as pd



df = pd.read_csv(path)

df['state'] = df['state'].str.lower()
df['total'] = df.Jan + df.Feb + df.Mar

sum_row = df[['Jan','Feb','Mar','total']].sum()

df_final = df.append(sum_row,ignore_index=True)

print(df_final)


# --------------
import requests
import pandas as pd

# Code starts here

url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response = requests.get(url)
df1=pd.read_html(response.content)[0]
df1=df1.iloc[11:,:]
df1 = df1.rename(columns =df1.iloc[0,:]).iloc[1:,:]
df1['United States of America'] = df1['United States of America'].apply(lambda x: x.replace(" ", "")).astype(object)
print(df1)


# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping = df1.set_index('United States of America')['US'].to_dict()
df_final.insert(6,'abbr',np.nan)
df_final['state'] = df_final['state']
df_final['abbr'] = df_final['state'].map(mapping)
df_final


# Code ends here


# --------------
# Code stars here

print(df_final[df_final['abbr'].isnull()==True])



df_mississipi = df_final[df_final['state'] == 'mississipi'].replace(np.nan, 'MS')

df_tenessee= df_final[df_final['state'] == 'tenessee'].replace(np.nan, 'TN')

df_final.replace(df_final.iloc[6],df_mississipi,inplace = True)

df_final.replace(df_final.iloc[10],df_tenessee,inplace = True)

print(df_mississipi)
# Code ends here


# --------------
# Code starts here

df_sub= df_final.groupby('abbr')[['Jan', 'Feb', 'Mar', 'total']].sum()

formatted_df = df_sub.applymap(lambda x : "${:,.0f}".format(x))

# Code ends here


# --------------
# Code starts here
sum_row = df[['Jan','Feb','Mar','total']].sum()

df_sub_sum = sum_row.transpose()

df_sub_sum = df_sub_sum.apply(lambda x : "${:,.0f}".format(x))

print(df_sub_sum)

final_table = formatted_df.append(df_sub_sum,ignore_index=True)

final_table.rename(index={13: 'Total'},inplace = True)

print(final_table)

#final_table.iloc[-1].set_index('Total')

# Code ends here


# --------------
# Code starts here
df_sub['total'].plot.pie()
plt.show()

# Code ends here


