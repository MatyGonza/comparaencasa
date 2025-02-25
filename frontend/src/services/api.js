export const fetchResults = async (query) => {
    try {
      console.log(`Fetching results for query: ${query}`);
      const response = await fetch(`http://localhost/miapp/api/search/?q=${query}`);
      const data = await response.json();
    ;
      console.log('Data received:', data);
      return data || [];
      
    } catch (error) {
      console.error('Error fetching data:', error);
      return [];
    }
  };